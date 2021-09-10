from django.contrib.auth.models import User

from barcodes.models import AppUser, Recipe, Log, Item
from barcodes.serializers import AppUserSerializer, RecipeSerializer, LogSerializer, ItemSerializer
from barcodes.permissions import IsOwnerOrReadOnly

from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class AppUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()

# class SnippetViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly, )
#
#     @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
