# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class dojos(models.Model): #should possibly be capital and non-plural
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.city)
class ninjas(models.Model):
    dojos = models.ForeignKey(dojos, related_name="ninjas",null=True)
    '''needs to be null because a new column is created in a current dataset.
    New column can't be empty, so it is set to null, and set to True because
    its okay to be null.'''
    #author = models.ForeignKey(Author, related_name="books")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.first_name, self.dojos)
#     comment = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     # Notice the association made with ForeignKey for a one-to-many relationship
#     # There can be many comments to one blog
#     blog = models.ForeignKey(Blog, related_name = "comments")
# class Admin(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     blogs = models.ManyToManyField(Blog, related_name = "admins")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)