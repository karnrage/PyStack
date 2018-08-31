from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^create$', views.create, name = 'create'),
   url(r'^delete_course/(?P<course_id>\d+)$', views.delete_course, name = 'delete_course'),
]
