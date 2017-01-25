from django.conf.urls import include, url
from django.contrib import admin
from community.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'studyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^write/', write, name='write'),
    url(r'^list/', list, name='list'),
    url(r'^view/(?P<num>[0-9]+)/$', view),
]
