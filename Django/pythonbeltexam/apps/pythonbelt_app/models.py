# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.

class BlogManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "first name should be more than 1 character"
            # was name instead of first name length
        if len(postData["username"]) < 3:
            errors["username"] = "last name should be more than 1 character"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"
        
        if not re.match(NAME_REGEX, postData['name']):
            errors["name"] = ("invalid first name")
        if not re.match(NAME_REGEX, postData['username']):
            errors["username"] = ("invalid username name")
        # if User.objects.filter(email = postData ['emailreg']).exists():
        #     errors ['emailreg'] = "email already registered"
        if len(postData['username']) < 2:
            errors["username"] = "username needs to be longer than 2 char"
        if (User.objects.filter(username = postData['username']).exists()):
            errors['username'] = "username taken already"
        if postData['bday'] == None:
            errors['bday'] = "Invalid DOB"
        
        
        return errors
        try:
            User.objects.get(email = postData['username'])
            errors['username'] = "The username is already taken"
        except:
            pass
        return
    def log_validator(self, postData): #need to finish
        errors = {}
        user = User.objects.get(username=postData['username']) # models needs to be =postData, no request, because passing in variable of postdata
        #hashcheck = None python not needed?
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"
            # was name instead of first name length
        if len(User.objects.filter(username = postData['username'])) < 0:
            correct_user = User.objects.filter(username = postData["username"])
        hash1 = bcrypt.checkpw(postData['password'].encode('utf8'), user.password.encode('utf8'))
        if hash1 == False:
            errors ['password'] = "Wrong password"
           # errors["email"] = "Blog name should be more than 1 character"
        # if type
        # if len(postData['desc']) < 10:
            # errors["desc"] = "Blog desc should be more than 10 characters"
        return errors

class RelationManager(models.Manager):
    def friend_validator(self, id1, id2):
        errors = {}
        if (id1 == id2):
            errors["friend1_id"] = "Friendship requires two different people"
        elif (User.objects.filter(friend1_id = int(id1), friend2_id = int(id2)).exists()):
            errors["friend1_id"] = "You two aren't strangers"
        # elif (User.objects.filter)
        return errors

   

class User(models.Model):
    #everything...... variables are case sensitive
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    wish = models.ManyToManyField("self", blank=True, related_name="friended_me")
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    hired = models.DateField(null=True)
    # Format='%m/%d/%y' not needed in datefield ( here ) above
    # objects = RelationManager()
    objects = BlogManager()

class Wish(models.Model):
    name = models.CharField(max_length=255)
    wanted = models.ForeignKey(User, related_name="wanted_by") 




   

