# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User, Item
import bcrypt

# Create your views here.


# def index(request):
#    response = "Hello, I am your first request!"
#    return HttpResponse(response)
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)

def create(request):
    errors = User.objects.reg_validator(request.POST)
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    else:
        name = request.POST['name']
        username = request.POST['username']
        
        password = request.POST['password']
        hired = request.POST['hired']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(name=name, password=hashed, username=username, hired=hired)#need to pass in hashed password into database alias=alias,
        request.session["id"] = person.id
        person.save()
        print "registrant was created"
        return redirect("/homepage") # do not render to POST, could get lost in loop
        #now redirct to route that handles sucess page 
        #return redirect('/')

def login(request):
    errors = User.objects.log_validator(request.POST)
    user = User.objects.get(username=request.POST['username'])
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
    users = User.objects.all()
    items = Item.objects.filter(wished_by=user)
    # print Item.objects.filter().wished_by    
    otherwishlist = Item.objects.exclude(wished_by=user)
    # mylist = User.most_wanted.wished_by(id=user.id)
    #take whole object and filter on html 
    #make seperate context items to easily loop through items
    context = {
        'user': User.objects.get(id=request.session['id']),
        'otherwishlist' : otherwishlist,
        'items' : items,
        # 'mylist' : mylist,

    }
    
    return render (request, "homepage.html", context) 

#handles form sub
#save items here
def new_wish(request):
#default process is to grab the current user id first, when creating item in database
#next the objects foreign key, in this case the name, needs to be created. with each parameter passed on 
    
    user = User.objects.get(id=request.session['id'])
    name = Item.objects.create(name=request.POST["item_name"], created_by=user)
    # IntegrityError: wishlist_app_item.created_by_id may not be NULL
    #had name first, but threw above error. Need user id for foreign key created_by
   


    # response = "Hello, I am your wishlist page!"
    # return HttpResponse(response)
    return redirect('/homepage')

#serves up page
#load items here
def add_wish_page(request):
    # items = Item.objects.all()
    # print items
    # context = {
    #     'items': items
    #     # Item.objects.get(id=request.session['id'])
    # }
    return render(request, 'new_wish.html')
# , context)

def item_profile_page(request, item_id):
    # user = User.objects.get(id=request.session['id'])
    
    current_items = Item.objects.get(id=item_id)
    this_item = current_items.wished_by.all()
    # print current_items.wished_by.f
    # print users_who_liked
    # users_who_liked = User.objects.filter(most_wanted=item)

    # for x in users_who_liked:
    #     print x
    context = {
        # 'item': item,
        # 'user' : user, 
        'item' : Item.objects.get(id=item_id), 
        'this_item' : this_item,
              
    }
    return render(request, 'item_profile.html', context)

def add_to_list(request, item_id):
    user = User.objects.get(id=request.session['id'])
    item = Item.objects.get(id=item_id)
    item.wished_by.add(user)
    item.save()

    return redirect('/homepage')

def also_added_to_wishlist(request, item_id):
    user = User.objects.get(id=request.session['id'])
    item = Item.objects.get(id=item_id)
    wanted_by = Item.objects.all()

    #when doing reverse lookup using related name need to put
    #related name after user class
    # also_wished = Item.wished_by.filter(id=item_id)

    # this_publisher.books.add(this_book)
    
    return redirect ('/')

def remove(request, item_id):
    user = User.objects.get(id=request.session['id'])
    item = Item.objects.get(id=item_id)
    item.wished_by.remove(user)
    item.save()

    return redirect('/homepage')

def logout(request):
    request.session.clear()
    return redirect('/')
