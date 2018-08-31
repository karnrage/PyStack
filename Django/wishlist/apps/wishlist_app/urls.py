from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^create$', views.create, name = 'create'),
   url(r'^homepage$', views.homepage, name = 'homepage'), #views.py needs to have a matching "def homepage"
   url(r'^login$', views.login, name = 'login'),
   url(r'^logout$', views.logout, name = 'logout'),
   url(r'^new_wish$', views.new_wish, name = 'new_wish'),
   url(r'^add_wish_page$', views.add_wish_page, name = 'add_wish_page'),
   url(r'^item_profile_page/(?P<item_id>\d+)$', views.item_profile_page, name = 'item_profile_page'),
   url(r'^add_to_list/(?P<item_id>\d+)$', views.add_to_list, name = 'add_to_list'),
   url(r'^remove/(?P<item_id>\d+)$', views.remove, name = 'remove'),


#    /(?P<id>\d+)


]
