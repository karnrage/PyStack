# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog" )
def create(request):
    return redirect("/")
def show(request, numbers):
    return HttpResponse("placeholder to later display all the list of blog "+str(numbers))
def edit(request, numbers):
    return HttpResponse("placeholder to edit blog "+str(numbers))
def delete(request, numbers):
    return redirect("/")
