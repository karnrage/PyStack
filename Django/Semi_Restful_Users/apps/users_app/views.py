# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Users
from django.contrib import messages

# Create your views here.

def index(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }
    return render(request,"index.html", context)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    Users.objects.create(first_name=first_name,last_name=last_name,email=email)
    print "user was created"
    return redirect('/')

def new(request):
    return render(request, "new.html")

def show(request, user_id):
    print "show page working"
    context = {
        'user': Users.objects.get(id=user_id),
    }
    return render(request, "show.html", context)

def edit(request,user_id):
    context = {
        'user': Users.objects.get(id=user_id),
    }
    return render(request,"edit.html", context)

def update(request, user_id):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/user/{}/edit'.format(user_id))
    else:
        user_to_update = Users.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        return redirect('/')

def delete(request, user_id):
    Users.objects.get(id=user_id).delete()
    return redirect('/')
