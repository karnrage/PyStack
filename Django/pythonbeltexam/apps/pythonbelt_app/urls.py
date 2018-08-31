from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [     
    #name of <form acton= xxx> goes in first place. ( after r'^ ). 
    url(r'^$', views.index, name = 'index'),
    #everytime a new user created, they are by default given an id
    # using this we can change the route be dynamic as below
    url(r'^create$', views.create, name = "create"), #in views need to have a route with the same name
    url(r'^homepage$', views.homepage, name = 'homepage'), # routing, now routing to 'whatever' definition. make a new 'whatever' def on views page
    url(r'^login$', views.login, name = 'login'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^add/(?P<id>\d+)$', views.add, name = 'add'),
    url(r'^erase/(?P<id>\d+)$', views.erase, name = 'erase'),
    url(r'^profile/(?P<id>\d+)$', views.profile, name = 'profile')
]
