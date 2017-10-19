# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Inside models.py
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField(default=70)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# class Comment(models.Model):
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