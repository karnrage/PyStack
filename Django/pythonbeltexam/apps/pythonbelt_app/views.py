# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User
import bcrypt
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    users = User.objects.all()
    context = {
        'users': users
    }
  # return HttpResponse(response)
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
        # email = request.POST['emailreg']
        password = request.POST['password']
        hired = request.POST['bday']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(name=name, username=username, password=hashed, hired=hired)#need to pass in hashed password into database alias=alias,
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
        # changed to redirect because 
    #errors = Users.objects.login_validator(request.POST)
    #password = request.post['password']

def homepage(request): #request is default parameter
    current_user = User.objects.get(id=request.session['id'])#current_user will be used in homepage welcoming
    users = User.objects.all()
    # wish = User.objects.exclude(wish=current_user).exclude(id=current_user.id)
    context = {
        # 'wish' : User.objects.exclude(wish=current_user).exclude(id=current_user.id),
        'wish' :current_user.wish.all(),
        'current_user' : current_user,
    }
     #'users': User.objects.get(id=request.session['id'])
    return render (request, "homepage.html", context) 

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request, id):
    
    #id=id<---- second id needs to match parameter req'd by function
     #reverse is for traversing through things
     #something in context taking in not showing
    context = {
        'friend' : User.objects.get(id=id)#whatever in quotes gets sent to html file.
    }
    response = "Hello, I'm creeping on your profile!"
    return render(request, 'friendsinfo.html', context)


def add(request, id):
    friend = User.objects.get(id=id)
    #when referring to the current user who is logged in, use below
    current_user = User.objects.get(id=request.session['id'])
    #create a relation between current user and friend
    current_user.friend.add(friend)
    #not saved until
    current_user.save()
    #now create relation between friend and user
    friend.friend.add(current_user)
    friend.save()
    print friend.name
    response = "Hello, I am your new friend!"
    #try to send back to page we are already at, so below
    print current_user.friend
    context = {
        'users' : User.objects.exclude(friend=current_user).exclude(id=current_user.id),
        'friends' :current_user.friend.all(),
        'current_user' : current_user,
    }
    # return render(request, 'homepage.html', context)
    return redirect('/add', context)
   


 
def erase(request, id):
    stranger = User.objects.get(id=id)
    current_user = User.objects.get(id=request.session['id'])
    current_user.friend.remove(stranger)
    current_user.save()
    stranger.friend.remove(current_user)
    stranger.save()
    context = {
        'friends' : User.objects.all()
    }
    return redirect('/homepage', context)
#
    


