from rest_framework import serializers
from barcodes.models import AppUser, Recipe, Log, Item
from django.contrib.auth.models import User

class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(many=True, view_name='recipe-detail', read_only=True)
    log = serializers.HyperlinkedRelatedField(many=True, view_name='log-detail', read_only=True)

    class Meta:
        model = AppUser
        fields = ['url', 'id', 'username', 'recipe', 'log']

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    data = serializers.HyperlinkedRelatedField(many=True, view_name='recipe-detail', read_only=True)

    class Meta:
        model = Recipe
        fields = ['url', 'id', 'owner', 'data']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    log = serializers.HyperlinkedRelatedField(many=True, view_name='log-detail', read_only=True)

    class Meta:
        model = Log
        fields = ['url', 'id', 'owner', 'data']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']

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
