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
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'exam/index', context)
