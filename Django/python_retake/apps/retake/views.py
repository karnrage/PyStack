# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User, Poke
# need to import models above. for example in wishlist< User, Item >were the models. 
# then erase 
import bcrypt



def index(request):
    # users = User.objects.all()
    # context = {
    #     'users': users
    # }
    return render(request, 'index.html')
# , context)

def create(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    else:
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['emailreg']                
        password = request.POST['password']
        bday = request.POST['bday']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(name=name, password=hashed, email=email, alias=alias, bday=bday)#need to pass in hashed password into database alias=alias,
        request.session["id"] = person.id
        person.save()
        print "registrant was created"
        return redirect("/homepage") # do not render to POST, could get lost in loop
        #now redirct to route that handles sucess page 
        #return redirect('/')

def login(request):
    errors = User.objects.log_validator(request.POST)
    user = User.objects.get(email=request.POST['emaillog'])
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect( "/")
    else:
        bcrypt.checkpw('password'.encode('utf8'), user.password.encode('utf8'))
        request.session['id'] = user.id

        return redirect( "/homepage")


def homepage(request): #request is default parameter
    user = User.objects.get(id=request.session['id'])
    print user
    all_users = User.objects.all()
    #print all_users
    other_users = User.objects.all().exclude(id=request.session['id'])
    #print other_users
    all_pokes =  Poke.objects.all()
    #print all_pokes
    poke_count = Poke.objects.filter(poke_to=request.session['id'])
    #print poke_count
    poked_you_list = Poke.objects.all().filter(poked_by=request.session['id']).exclude(id=request.session['id'])
    #print poked_you_list
    
    
    
    # otherwishlist = Item.objects.exclude(wished_by=user)
    # mylist = User.most_wanted.wished_by(id=user.id)
    #take whole object and filter on html 
    #make seperate context items to easily loop through items
    context = {
        'user': user,
        #
        'other_users': other_users,
        'all_pokes': all_pokes,
        'poke_count': poke_count,
        'poked_you_list': poked_you_list,
        

    }
    
    return render (request, "homepage.html", context) 

# FIRST TRY BELOW

# def poke(request):
#     user = User.objects.get(id=request.session['id'])
#     print user
#     #getting user id       
#     pokers = Poke.objects.filter(got_poked=user).order_by(-Poke.numberPokes)
#     print pokers
#     # getting the number of people who poked the user, and arranging them descending
#     pplnum = len(pokers)
#     print pplnum
#     #got number of people who poked user by getting length of column

#     users_to_poke = User.objects.filter(id = user.id)
#     print users_to_poke
    
#     context = {
#         'pplnum' : pplnum,
#         'user': user,
#         'users_to_poke' : users_to_poke,
#         'you_poked' : pokers
#     } 

#     return render(request, '/homepage.html', context)

def poke(request, user_id):

    user_poke_other = User.objects.get(id=request.session['id'])
    got_poked = User.objects.get(id=user_id)
    poke = Poke()
    poke.poker_to = got_poked
    poke.poked_by = user_poke_other
    poke.numberPokes+=1
    poke.save()
    
    return redirect('/homepage')


# #SECOND TRY BELOW

# def poke(request):
#     user = User.objects.get(id=request.session['id'])
#     print user
#     #getting user id       
#     pokers = Poke.objects.filter(got_poked=user).order_by('-numberPokes')
#     print pokers
#     # getting the number of people who poked the user, and arranging them descending
#     pplnum = len(pokers)
#     print pplnum
#     #got number of people who poked user by getting length of column

#     # users_to_poke = User.objects.filter(~Q(id = user.id))
#     users_to_poke = User.objects.filter(id = user.id)
#     print users_to_poke
    
#     context = {
#         'pplnum' : pplnum,
#         'user': user,
#         'users_to_poke' : users_to_poke,
#         'you_poked' : pokers
#     } 

#     return redirect('/homepage.html')

# def pokeUser(request, user_id):

#     Poke.objects.pokeUser(user_id, request.session['id'])

# render(request, '/homepage.html', context)
#     return redirect(reverse('poke:pokes'))


def logout(request):
    request.session.clear()
    return redirect('/')
