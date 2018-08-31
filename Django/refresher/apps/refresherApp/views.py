from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
# need to import models above. for example in wishlist< User, Item >were the models. 
# then erase *
# import bcrypt

def index(request):
   response = "Hello, I am your first request!"
   return HttpResponse(response)


# Create your views here.
