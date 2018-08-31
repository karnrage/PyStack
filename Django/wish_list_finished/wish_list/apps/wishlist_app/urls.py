from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addingitem/$', views.addingitem_page, name="addingitem_page"),
    url(r'^submititem/$', views.submit_item, name="submititem"), 
    url(r'^wishlist/(?P<Item_id>\d+)$', views.show, name="show"),
    url(r'^adding/(?P<Item_id>\d+)$', views.add_tolist, name="adding"),
    url(r'^wishlist/(?P<Item_id>\d+)/destroy$', views.destroy), 
    url(r'^clear/$', views.clear, name="clear"),
]