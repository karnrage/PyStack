from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^register$', views.register, name = 'register'),
   url(r'^login$', views.login, name = 'login'),
   url(r'^logout$', views.logout, name = 'logout'),
   url(r'^homepage$', views.homepage, name = 'homepage'), #views.py needs to have a matching "def homepage"
   url(r'^add_wish_link$', views.add_wish_link, name = 'add_wish_link'),
   url(r'^add_wish_page$', views.add_wish_page, name = 'add_wish_page'),
   
   
]