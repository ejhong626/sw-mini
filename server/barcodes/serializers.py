import operator
from functools import reduce
from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.urls import reverse

from barcodes.models import Item, Recipe, Log

# class MultipleFieldLookupMixin:
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#     def get_object(self):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, **filter)  # Lookup the object
#         self.check_object_permissions(self.request, obj)
#         return obj

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ingredients = ItemSerializer(many=True)
    # ingredients = serializers.HyperlinkedRelatedField(many=True,view_name='recipe-detail')

    class Meta:
        model = Recipe
        fields = ['url', 'id', 'owner', 'title', 'ingredients']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    data = ItemSerializer(many=True)

    class Meta:
        model = Log
        fields = ['url', 'id', 'owner', 'data', 'created']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        many=True, view_name='recipe-detail', read_only=True)
    log = serializers.HyperlinkedRelatedField(
        many=True, view_name='log-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'recipe', 'log']

# from barcodes.jsonserial import DataFieldsSerializer

# class BarcodeSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='barcode-highlight', format='html')
#
#     class Meta:
#         model = Barcode
#         fields = ['url', 'id', 'highlight', 'owner',
#                   'title', 'code', 'linenos', 'language', 'style']
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     barcodes = serializers.HyperlinkedRelatedField(many=True, view_name='barcode-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'barcodes']
