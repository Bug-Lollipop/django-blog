#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^grappelli/',include('grappelli.urls')), #放admin前面优先加载  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('blog.urls')),
    url(r'^search/',include('haystack.urls')),
    url(r'^register/$', 'blog.views.register'),
)
