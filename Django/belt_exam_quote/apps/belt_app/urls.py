from django.conf.urls import url 
from .import views
urlpatterns = [
    url (r'^$', views.index , name="index"),
    url (r'^register$', views.register, name="register"),
    url (r'^login$', views.login, name="login"),
    url (r'^logout$', views.logout, name="logout "),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^user_info/(?P<id>\d+)/$', views.user_info, name="user_info"),
    url(r'^favorites/(?P<id>\d+)/$', views.favorites, name="favorites"),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name="remove"),
    url(r'^add_quote$', views.add_quote, name="add_quote"),
]