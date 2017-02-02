from django.contrib.auth.models import User
from requests import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permission import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    여기에 `highlight` 기능의 코드만 추가로 작성했습니다
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    이 뷰셋은 `list`와 `detail` 기능을 자동으로 지원합니다
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

