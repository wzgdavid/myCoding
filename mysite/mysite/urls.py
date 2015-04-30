#encoding utf-8
'''
file: urls.py
'''

from django.contrib import admin
from django.conf.urls import include, patterns, url



urlpatterns = patterns('mysite.views.main',
    url(r'^api/$', 'api', name='api'),
    url(r'^api2/$', 'api2', name='api2'),
)