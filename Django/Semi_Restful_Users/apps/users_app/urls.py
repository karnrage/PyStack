from django.conf.urls import url, include
from django.contrib import admin
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^new$', views.new, name = "new"),
    url(r'^user/(?P<user_id>\d+)$', views.show, name = 'show'),
    url(r'^user/(?P<user_id>\d+)/edit$', views.edit, name = 'edit'),
    url(r'^user/(?P<user_id>\d+)/update$', views.update, name = 'update'),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete, name = 'delete')
]
