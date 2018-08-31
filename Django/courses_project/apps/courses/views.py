# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
# need to import models above. for example in wishlist< User, Item >were the models
import bcrypt

def index(request):
    # response = "Hello, I am your first request!"
    # courses = Course.objects.all()
    

    course_detail = Course.objects.all()
    print course_detail
    desc_detail = Description.objects.all()
    print desc_detail

    context = {
        "course" : course_detail,
        "desc" : desc_detail,
    }
    
    return render(request, 'index.html', context)

def create(request):
    school_class = Course.objects.create(name=request.POST["course"])
    description_of = Description.objects.create(desc=request.POST["description"], description_about=school_class)
    
    return redirect('/')

# def read(request):
#     course_detail = Course.objects.all()
#     print course_detail
#     desc_detail = Course.objects.get(description_about=Course)
#     print desc_detail

#     context = {
#         "course" : course_detail,
#         "desc" : desc_detail,
#     }
    
#     return render(request, "index.html", context)


def remove_page(request):

   response = "Hello, I am your first request!"
   return HttpResponse(response)


def delete_course(request, course_id):
    # specific_course = Course.objects.filter(id=course_id)
    # Course.save()
    # print specific

    # specific.delete()
    # specific.save()


    specific_description = Description.objects.filter(id=course_id)
    specific_description.delete()

    remove(id=Course.course_descrip.id)

    return redirect('/')

#delete relationship first, then delete row