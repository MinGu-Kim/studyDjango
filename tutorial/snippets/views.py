from django.http import Http404
from requests import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.generics import GenericAPIView

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class snippets_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
