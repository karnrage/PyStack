# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#? import views?
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class BlogManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["firstname"]) < 2:
            errors["firstname"] = "first name should be more than 1 character"
            # was name instead of first name length
        if len(postData["alias"]) < 2:
            errors["alias"] = "last name should be more than 1 character"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"
        if not re.match(EMAIL_REGEX, postData['emailreg']):
            errors["emailreg"] = ("invalid email")
        if not re.match(NAME_REGEX, postData['firstname']):
            errors["firstname"] = ("invalid first name")
        if not re.match(NAME_REGEX, postData['alias']):
            errors["alias"] = ("invalid last name")
        if User.objects.filter(email = postData ['emailreg']).exists():
            errors ['emailreg'] = "email already registered"
        
        return errors
        try:
            User.objects.get(email = postData['emailreg'])
            errors['emailreg'] = "The email is already taken"
        except:
            pass
        return
    def log_validator(self, postData): 
        errors = {}
        user = User.objects.get(email=postData['emaillog']) # models needs to be =postData, no request, because passing in variable of postdata
        
        # --------------------------------------------------
        try:
             User.objects.filter(email = postData ['emailreg']).exists()
        except:
             errors['nonexistant'] = "user does not exist"  
            #  --------------------------------------------------          
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"
            # was name instead of first name length
        if len(User.objects.filter(email = postData['emaillog'])) < 0:
            correct_user = User.objects.filter(email = postData["emaillog"])
        hash1 = bcrypt.checkpw(postData['password'].encode('utf8'), user.password.encode('utf8'))
        if hash1 == False:
            errors ['password'] = "Wrong password"
        return errors
    ##################################################################################
    ####################### new validator for review form #################

    # def form_validator(self, postData):
    #     #setting an empty dictionary, using dict instead of array cause array breaks
    #     errors = {} 
    #     if len(postData["book"]) < 2:
    #         errors["book"] = "first name should be more than 1 character"
    #     ########checking if authoer length is valid    
    #     if len(postData["author"]) < 2:
    #         errors["alias"] = "last name should be more than 1 character"        
    #     # if not re.match(EMAIL_REGEX, postData['emailreg']):
    #     #     errors["emailreg"] = ("invalid email")
    #     if not re.match(NAME_REGEX, postData['book']):
    #         errors["book"] = ("invalid book title")
    #     if not re.match(NAME_REGEX, postData['author']):
    #         errors["author"] = ("invalid author name")
    #     if Create_book.objects.filter(email = postData ['book']).exists():
    #         errors ['booktitle'] = "book already reviewed"        
    #     return errors

#below not needed in case a user wished to review a book more than once
        # try:
        #     User.objects.get(review = postData['book'])
        #     errors['emailreg'] = "The email is already taken"
        # except:
        #     pass
        return


class User(models.Model):
    firstname = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # confirm = models.CharField(max_length=255) #not needed cause only need to save password
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    reviews = models.IntegerField()
    objects = BlogManager()

class Create_book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]) #imported django built in validator to use min/max range
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    # related name must be in quotes .....string format
    commentedby = models.ForeignKey(User, related_name="commentedBooks")

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    






        


