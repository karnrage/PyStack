from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^create$', views.create, name = 'create'),
   url(r'^homepage$', views.homepage, name = 'homepage'), #views.py needs to have a matching "def homepage"
   url(r'^login$', views.login, name = 'login'),
   url(r'^logout$', views.logout, name = 'logout'),
   
   url(r'^poke/(?P<user_id>\d+)$', views.poke, name = 'poke'),

]
