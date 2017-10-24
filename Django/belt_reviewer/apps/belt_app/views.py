# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User
import bcrypt
# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
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
        firstname = request.POST['firstname']
        alias = request.POST['alias']
        email = request.POST['emailreg']
        password = request.POST['password']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(firstname=firstname, alias=alias, email=email, password=hashed)#need to pass in hashed password into database
        request.session["id"] = person.id
        person.save()
        print "registrant was created"
        return redirect("/success")

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

        return redirect( "/success")

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book (request):

    return redirect ('/')

def home(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def make_review(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)