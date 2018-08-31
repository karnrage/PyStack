# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
import bcrypt
from django.contrib import messages
from .models import Users, Favorite, Quote


def index (request):
  
    return render(request ,'index.html') 


def dashboard(request):

    context = {
    "user": Users.objects.get(id=request.session["id"]),
    "quotes": Quote.objects.all(),
    "favorites":Favorite.objects.filter(user__id=request.session["id"])
    }
    return render(request,'dashboard.html', context)

def user_info(request, id):
    context = {
    "user":Users.objects.get(id=id),
    "posts":Quote.objects.all().filter(user=id)
    }
    return render(request,'userinfo.html', context)


def register (request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    confirm_password = request.POST['confirm_password']
    errors = Users.objects.basic_validator(request.POST)
    if len (errors) :
        for tag, error in errors.iteritems():
            messages.error(request, error)            
            return redirect('/')
    else:
        user = Users.objects.create(first_name=first_name, last_name=last_name,email=email, password=hashed_password, confirm_password=confirm_password)
        request.session['id'] = user.id
        return redirect ('/dashboard')

def login (request):
    errors = Users.objects.login_validator(request.POST)
    password = request.POST['password']

    if len (errors) :
        for tag, error in errors.iteritems():
            messages.error(request, error)            
            return redirect('/')
    else:
        user = Users.objects.get(email=request.POST['email'])
        request.session['id']=user.id
        return redirect ('/dashboard')



def add_quote(request):
        author = request.POST.get("author")
        message = request.POST.get("message")
        user = Users.objects.get(id=request.session["user_id"])
        quote = Quote.objects.create(author=author, message=message, user=user)
        return redirect ("/dashboard")
    
def favorites(request, id):
    user = User.objects.get(id=request.session["id"])
    quote = Quote.objects.get(id=id)
    favorite = Favorite.objects.create(
    quote = quote,
    user = user,
    )
    request.session["fav"]=favorite.quote.id
    return redirect ("/dashboard")

def remove(request, id):
    favorite=Favorite.objects.filter(id=id)
    favorite.delete()
    return redirect("/dashboard")


def logout (request):
    request.session.clear()
    return redirect ('/')
# Create your views here.
