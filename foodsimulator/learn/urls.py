from django.conf.urls import patterns, include, url
from django.contrib import admin
from learn.views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GamingPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',index,name="dummy_view"),
    url(r'^save_data/',save_data,name="save_view"),
    url(r'^home/',home,name="home_view"),
)

