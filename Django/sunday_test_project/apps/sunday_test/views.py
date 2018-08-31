# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
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
        for error in errors:
            messages.error(request, error)
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
        request.session["user_id"] = person.id
        person.save()
        messages.success(request, "You've successfully registered")
        print "registrant was created"
        return redirect("/homepage")
        #do not render to POST, could get lost in loop
        #now redirct to route that handles success page 

def login(request):
    errors = User.objects.log_validator(request.POST)
    password = request.POST['password']
    try:
        user_login = User.objects.get(alias=request.POST['alias'])
    except Exception:
        errors.append('Email not in our database')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')

    password_check = bcrypt.checkpw(password.encode(), user_login.password.encode())

    if password_check == True:
        request.session['name'] = user_login.name
        request.session['user_id'] = user_login.id
        messages.success(request, "You've successfully logged in")
        return redirect('/homepage')
    else:
        errors.append('Email/Password is incorrect')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')


def homepage(request): 
    # try:
        user = User.objects.get(id=request.session['user_id'])
        
        all_users = User.objects.all()
        #print all_users
        other_users = User.objects.all().exclude(id=request.session['user_id'])
        #print other_users    
        
        #take whole object and filter on html 
        #make seperate context items to easily loop through items


        your_trips = Trip.objects.filter(user=user)
        other_trips = Trip.objects.exclude(user=user)
        context = {
            'user': user,
            'other_trips': other_trips,
            'your_trips': your_trips,        
        }    
        return render (request, "homepage.html", context)
    # except:
        
        # return redirect('/')

def create(request):
    

    return render(request, "addtrip.html")

def collect_data(request):
    errors = Trip.objects.validate_trip(request.POST)
    location = request.POST["location"]
    description = request.POST["description"]
    date_from = request.POST["date_from"]
    date_to = request.POST["date_to"]
    current_user = User.objects.get(id=request.session["user_id"])

    if len(errors):
        for error in errors:
            messages.warning(request, error)
        return redirect ('/create')
    else:

        Trip.objects.create(location=location, description=description, date_from=date_from, date_to=date_to, user=current_user)

        return redirect('/homepage')

def trip_profile(request, trip_id):

    current_trip = Trip.objects.get(id=trip_id)
    print current_trip
    other_users = current_trip.users.exclude(id=current_trip.user.id)
    print other_users
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'other_users': other_users,
    }
    return render(request, "profile.html", context)

def join_trip(request, trip_id):
    current_user = User.objects.get(id=request.session['user_id'])
    current_trip = Trip.objects.get(id=trip_id)
    current_trip.users.add(current_user)
    current_trip.save()
    # give confirmation of joining trip
    messages.success(request, "Pack your bags!!!")

    return redirect('/homepage')


def logout(request):
    request.session.clear()
    return redirect('/')