# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
import bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        # Length of inputs--------------
        if len(postData["name"]) < 3:
            errors["name"] = "first name should be more than 3 characters"
        # uncomment below if using last name and comment out alias postData
        # if len(postData["last_name"]) < 3:
        #     errors["last_name"] = "last name should be more than 3 characters"            
        if len(postData["alias"]) < 3:
            errors["alias"] = "alias name should be more than 3 characters"        
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"

        #  If inputs are valid characters
        if not re.match(EMAIL_REGEX, postData['emailreg']):
            errors["emailreg"] = ("invalid email")
        if not re.match(NAME_REGEX, postData['name']):
            errors["name"] = ("invalid first name")
        if not re.match(NAME_REGEX, postData['alias']):
            errors["alias"] = ("invalid alias")

        # If alias already exists
        if User.objects.filter(alias = postData ['alias']).exists():
            errors ['alias'] = "alias already registered"
        
        return errors
        try:
            User.objects.get(email = postData['emailreg'])
            errors['emailreg'] = "The email is already taken"
        except:
            pass
        return




    def log_validator(self, postData): 
        errors = {}
        try: 
        # models needs to be =postData, no request, because passing in variable of postdata
            user = User.objects.get(email=postData['emaillog'])
        except:
            errors['nonexistant'] = "user does not exist"               
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"            
        if len(User.objects.filter(email = postData['emaillog'])) > 0:
            correct_user = User.objects.filter(email = postData["emaillog"])[0]
            # need to make [0] since a list needs a starting point            
        if errors:
            return errors
        hash1 = bcrypt.checkpw(postData['password'].encode('utf8'), user.password.encode('utf8'))
        if hash1 == False:
            errors ['password'] = "Wrong password"
        return errors    
        return


class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "item name should be more than 3 characters"
        if len(postData["name"]) == 0:
            errors["name"] = "item name cannot be blank"
        
        return errors    
        return

class User(models.Model):    
    name = models.CharField(max_length=255)
    # username = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)    
    password = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    bday = models.DateField(null=True)      
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {} {}>".format(self.id, self.name, self.alias, self.password, self.createdat, self.updatedat)
    #need above to print in terminal
    

class Item(models.Model):
    #related_name must be a string
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name="who_added")
    wanted_by = models.ManyToManyField(User, blank=True, related_name="most_wanted")
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = ItemManager()
    def __repr__(self):
        return "<Item object: {} {} {} {} {} {}>".format(self.id, self.name, self.added_by, self.wanted_by, self.created_at, self.updated_at)
    #need above to print in terminal


