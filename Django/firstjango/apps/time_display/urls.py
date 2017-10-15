from django.conf.urls import url, include
from django.contrib import admin
from views import *


urlpatterns = [
    url(r'^$', index, name = 'index'), 
    #url(r'^new', new, name = 'new'),
    #url(r'^create', create, name = 'create'),
    #url(r'^(?P<numbers>[0-9]+)', show, name = 'show'),
    #url(r'^(?P<numbers>[0-9]+)/edit', edit, name = 'edit'),
    #url(r'^(?P<numbers>[0-9]+)/delete', delete, name = 'delete'),
        
]


