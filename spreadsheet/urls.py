from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('ssapp.urls')),
    url(r'^app/', include('ssapp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
