# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name should be more than 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name should be more than 2 characters"

        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "This email is invalid"
        
        if len(postData['password']) < 8:
            errors["password"] = "This password  is invalid"
        
        if postData['password'] != postData['confirm_password'] :
            errors["confirm_password"] = "This password  is invalid"

        if len(Users.objects.filter(email = postData['email'])) > 0:
            errors['email'] = "This email is already registered!"

        return errors

    def login_validator(self , postData):
        errors = {}
        if len(postData['password']) < 8:
            errors["password"] = "This password  is invalid"

        if len(Users.objects.filter(email = postData['email'])) < 1:
            errors['email'] = "This email is invalid!"
            return errors
        current_user = Users.objects.filter(email = postData['email'])[0]
        print current_user.password
        print postData['password']
        password_check = bcrypt.checkpw(postData['password'].encode(), current_user.password.encode())
        if password_check == False:
            errors['password'] = 'this is invalid password'
        return errors
class QuoteManager(models.Model):
    def quote_validator(self , postData):
        errors = {}
        if len (postData['author']) < 4:
            errors['author'] = "author name should be at least 3 characters"
        if len (postData['message']) < 11:
            errors['message'] = "message should be more than 10 characters"
        return errors


        


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    password =  models.CharField(max_length=255)
    confirm_password =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = UsersManager()
class Quote(models.Model):
    author = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(Users,related_name='quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

class Favorite(models.Model):
    user = models.ForeignKey(Users,related_name='favorites')
    quote = models.ForeignKey(Quote,related_name='favorites')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
# Create your models here.
