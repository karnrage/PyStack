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

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["firstname"]) < 2:
            errors["firstname"] = "first name should be more than 1 character"
            # was name instead of first name length
        if len(postData["lastname"]) < 2:
            errors["lastname"] = "last name should be more than 1 character"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"
        if not re.match(EMAIL_REGEX, postData['emailreg']):
            errors["emailreg"] = ("invalid email")
        if not re.match(NAME_REGEX, postData['firstname']):
            errors["firstname"] = ("invalid first name")
        if not re.match(NAME_REGEX, postData['lastname']):
            errors["lastname"] = ("invalid last name")
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
        try: 
            user = User.objects.get(email=postData['emaillog']) # models needs to be =postData, no request, because passing in variable of postdata
        except:
            errors['nonexistant'] = "user does not exist"               
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"
            # was name instead of first name length
        if len(User.objects.filter(email = postData['emaillog'])) > 0:
            correct_user = User.objects.filter(email = postData["emaillog"])[0]
            # need to make [0] since a list needs a starting point
            # errors["invalid"] = "user hasn't been registered yet"

        if errors:
            return errors
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
class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if (len(postData['author']) < 2): 
        # & (postData['authorsel'] == ""):
            errors["author"] = "Author should be more than 2 characters"
        if len(postData['title']) < 1:
            errors["title"] = "Title should exist"
        return errors

class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['description']) < 5:
            errors["description"] = "Description should be more than 5 characters"
        if (int(postData['rating']) < 0) | (int(postData['rating']) > 5):
            errors["rating"] = "Rating should be between 0 and 5"
        return errors

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # confirm = models.CharField(max_length=255) #not needed cause only need to save password
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    reviews = models.IntegerField()
    objects = UserManager()
#class name needs to be capitalized
class Book(models.Model):
    title = models.CharField(max_length=255)
    total_rating = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]) #imported django built in validator to use min/max range
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    # related name must be in quotes .....string format
    #related name is used to lookup from User by calling commentedBooks. So User.commentedBooks would find all commentedby books
    commentedby = models.ManyToManyField(User, related_name="commentedBooks")
    #, on_delete= models.CASCADE)
    review_public = models.IntegerField()
    objects = BookManager()
    #possibly comment out above
    

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    # objects = AuthorManager()
    #possibly comment out above

class Review(models.Model):
    review_user=models.ForeignKey(User,related_name="personal", on_delete= models.CASCADE)    
    review = models.CharField(max_length=255)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]) #imported django built in validator to use min/max range
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = ReviewManager()
    #possibly comment out above

    # if I do manytomany need .add like in friends app






        


