# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData["course"]) > 5:
            errors["course"] = "course name should be more than 3 characters"
        if len(postData["description"]) > 0:
            errors["description"] = "description should be more than 3 characters"
        
        return errors    
        return


class Course(models.Model):
    name = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()
#class name needs to be capital

class Description(models.Model):
    desc = models.CharField(max_length=255)
    #below only links to this model from above course. entering query for example of
    # Course.course_descrip ONLY connects to this table. Need to type Course.course_descrip.desc. to
    # get 
    id = models.CharField(primary_key=True, max_length=255, default=0)
    description_about = models.OneToOneField(Course, related_name='course_descrip')
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    # to start with the description table and get a attribute/column from the course
    # do Description.description_about.name <--name or createdat or objects
    # to start with the Course table and get a attribute/column from the description
    # do Course.course_descript.desc <--or id or description about or etc