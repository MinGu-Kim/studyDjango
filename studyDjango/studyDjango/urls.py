from django.conf.urls import include, url
from django.contrib import admin
from community.views import *
from blog.views import *
from post_service.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'studyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # community app
    url(r'^write/', write, name='write'),
    url(r'^list/', list, name='list'),
    url(r'^view/(?P<num>[0-9]+)/$', view),

    # REST framework
    url(r'^rest-api/', include('rest_framework.urls')),
    # REST framework swagger
    url(r'^rest-swagger/', include('rest_framework_swagger.urls')),

    # blog app
    url(r'^blog/', blog_page),

    # REST
    url(r'^api/blog/', blog_api.as_view()),

    # post_service app
    url(r'^board/', include('post_service.urls')),

    # user_manager app
    url(r'^user/', include('user_manager.urls'))
]
