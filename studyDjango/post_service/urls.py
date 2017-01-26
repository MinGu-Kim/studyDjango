from django.conf.urls import patterns, include, url
from post_service.views import *

urlpatterns = patterns('',
    url(r'^$', post_list)
)
