from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.db import models
import re
import bcrypt

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+$')
# ^[a-zA-Z0-9_.-]+$
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self,postData):
        errors = []
        if len(self.filter(username=postData['username'])) > 0:
            user = self.filter(username=postData['username'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                 errors.append ("Invalid password")
        else: 
            errors.append ("No such user")

        if errors:
            return errors

        return user

    def register_valid(self, postData):
        errors = []
        # -----------------------------------
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2 or len(postData['username']) < 2:
            errors.append("name/username fields must be at least 3 characters")
        #  -----------------------------------
        if len(postData['password']) < 4:
            errors.append("password must be at least 4 characters")
        #  -----------------------------------           
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('name fields must be letter characters only')
        #  -----------------------------------
        if not re.match(USERNAME_REGEX, postData['username']):
            errors.append("invalid username")
        #  -----------------------------------
        if len(User.objects.filter(username=postData['username'])) > 0:
            errors.append("username already in use")
        #  -----------------------------------
        if postData['password'] != postData['confirm_password']:
            errors.append("passwords do not match")

        if not errors:
            # hash password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                username=postData['username'],
                password=hashed,
                hired=postData['hired']
            )
            return new_user

        return errors

    def item_validator(self,postData):
        errors = []
        if len(postData['product']) == 0:
            errors.append("item field cannot be empty")
        elif len(postData['product']) < 2:
            errors.append("item name must be at least 3 characters")
        if len(Item.objects.filter(product=postData['product'])) > 0:
            errors.append("item already listed! check other users to add!")
        if errors:
            return errors
        # else:
        #     return product



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hired = models.DateField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.id, self.username, self.password, self.created_at, self.updated_at)

class Item(models.Model):
    product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_items", null=True)
    listed_by = models.ManyToManyField(User, related_name="listed_items")
    objects = UserManager()
    def __repr__(self):
        return "<Item object: {} {}>".format(self.product, self.uploader)