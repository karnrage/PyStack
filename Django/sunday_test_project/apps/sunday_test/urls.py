from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [ 
   url(r'^$', views.index, name = 'index'),
   url(r'^register$', views.register, name = 'register'),
   url(r'^login$', views.login, name = 'login'),
   url(r'^logout$', views.logout, name = 'logout'),
   url(r'^homepage$', views.homepage, name = 'homepage'), #views.py needs to have a matching "def homepage"
   url(r'^create$', views.create, name = 'create'),
   url(r'^collect_data$', views.collect_data, name = 'collect_data'),
   url(r'^trip_profile/(?P<trip_id>\d+)$', views.trip_profile, name = 'trip_profile'),
   url(r'^join_trip/(?P<trip_id>\d+)$', views.join_trip, name = 'join_trip'),
      
]