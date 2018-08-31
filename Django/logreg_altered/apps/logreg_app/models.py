# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


#did email, didn't do name

# Create your models here.

class BlogManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "name should be more than 1 character"
            # was name instead of first name length
        if len(postData["username"]) < 3:
            errors["username"] = "username should be more than 1 character"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"
        if not re.match(NAME_REGEX, postData['username']):
            errors["username"] = ("invalid username")
        if not re.match(NAME_REGEX, postData['name']):
            errors["name"] = ("invalid  name")
        if not re.match(NAME_REGEX, postData['username']):
            errors["username"] = ("invalid user name")
        if User.objects.filter(username = postData ['username']).exists():
            errors ['username'] = "username already registered"
        
        return errors
        try:
            User.objects.get(email = postData['emailreg'])
            errors['emailreg'] = "The email is already taken"
        except:
            pass
        return
    def log_validator(self, postData): #need to finish
        errors = {}
        user = User.objects.get(email=postData['emaillog']) # models needs to be =postData, no request, because passing in variable of postdata
        #hashcheck = None python not needed?
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"
            # was name instead of first name length
        if len(User.objects.filter(email = postData['emaillog'])) < 0:
            correct_user = User.objects.filter(email = postData["emaillog"])
        hash1 = bcrypt.checkpw(postData['password'].encode('utf8'), user.password.encode('utf8'))
        if hash1 == False:
            errors ['password'] = "Wrong password"          
        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)    
    password = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    hired = models.DateField(null=True)
    objects = BlogManager()
    

