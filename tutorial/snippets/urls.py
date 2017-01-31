from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import snippets_api

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/api', snippets_api.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)