from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^create$', views.create, name = "create"),
   #-----------new route below
   url(r'^home$', views.home, name = 'home'), 
   url(r'^make_review$', views.make_review, name = "make_review"),
   url(r'^add_book$', views.add_book, name = "add_book"),
   #-----------old routes again
   url(r'^login$', views.login, name = 'login'),
   url(r'^logout$', views.logout, name = 'logout')

]
# in views.py need def's with same name as route to avoid error