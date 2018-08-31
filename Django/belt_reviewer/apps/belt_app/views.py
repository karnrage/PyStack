# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User, Book, Author, Review

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
        lastname = request.POST['lastname']
        email = request.POST['emailreg']
        password = request.POST['password']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(firstname=firstname, lastname=lastname, email=email, password=hashed, reviews=0)#need to pass in hashed password into database
        request.session["id"] = person.id
        person.save()
        print "registrant was created"
        return redirect("/home")

def login(request):
    errors = User.objects.log_validator(request.POST)
    try:
        user = User.objects.get(email=request.POST['emaillog'])
    except:        
        errors['nonexistant'] = "user does not exist"
    
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect( "/")
    else:
        bcrypt.checkpw('password'.encode('utf8'), user.password.encode('utf8'))
        request.session['id'] = user.id

        return redirect( "/home")

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book (request):
    # errors = Book.objectsbasic_validator(request.POST)
    # errors = .objects.basic_validator(request.POST)

    # title = request.POST['book']
    # author = request.POST['author']
    # review = request.POST['item_id']

    return render(request, "add_book.html")
# , context)

#def login redirects to def home
def home(request):
    try:
        current_user = User.objects.get(id = request.session['id'])
        reviews = Book.objects.all().order_by('-createdat')[:3]
        your_reviews = Book.objects.filter(user = user.id).order_by('-createdat')
        if not reviews.exists():
            reviews = None
        if not your_reviews.exists():
            your_reviews = None
    except:
        pass
    # response = "Hello, I am your first request!"
    user = User.objects.all()
    books = Book.objects.all()
    #get attribute of commentedby and equal to the current user
    commentedby = Book.objects.filter(commentedby=user)    
    commentedbooks = Book.objects.filter(commentedby=user)
    nonrated = Book.objects.exclude(commentedby=user)
    personalreview = Review.objects.filter(review_user=user)

    #need to make query to pass into context
    #context only way to get stuff passed onto page
    context = {
        #right side is the query, left side is whatever is being passed
        'books': books,
        'users': user,
        'commentedbooks' : commentedbooks,
        'nonrated' : nonrated,
        'personal' : personalreview,
        'user': user,
        'current_user' : current_user

    }
    #if rendering xxxx.html req'd
    #do not put slash infront of /home.html
    return render(request, "home.html", context)

def make_review(request, book_id):
    #here, add current user to the book list of commentedby
     
    response = "Hello, I am your first request!"
    return HttpResponse(response)