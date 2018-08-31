# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User, Item
# need to import models above. for example in wishlist< User, Item >were the models. 
# then erase *
import bcrypt


# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)


def register(request):
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
        return redirect("/homepage")
        #do not render to POST, could get lost in loop
        #now redirct to route that handles success page 

def login(request):
    errors = User.objects.log_validator(request.POST)
    user = User.objects.get(alias=request.POST['username'])
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect( "/")
    else:
        bcrypt.checkpw('password'.encode('utf8'), user.password.encode('utf8'))
        request.session['id'] = user.id

        return redirect( "/homepage")


def homepage(request): 
    user = User.objects.get(id=request.session['id'])
    print user
    all_users = User.objects.all()
    #print all_users
    other_users = User.objects.all().exclude(id=request.session['id'])
    #print other_users    
    
    #take whole object and filter on html 
    #make seperate context items to easily loop through items
    context = {
        'user': user,
        'other_users': other_users,        
    }    
    return render (request, "homepage.html", context) 

#def can either lead to page or handle info. this lead to page
def add_wish_link(request): 
    
    return redirect( "/add_wish_page")

#def can either lead to page or handle info. this handles info

def add_wish_page(request):
    user = User.objects.get(id=request.session['id'])
    # print user
    name = Item.objects.create(name=request.POST["item_name"], added_by=user)
    # print name
    # name = Item.objects.create(name=request.POST['item'], added_by=user)

    return render (request, "add_page.html")
    #pages get file name in quotes, routes get /


def logout(request):
    request.session.clear()
    return redirect('/')