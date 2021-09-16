import json

from barcodes.models import Item, Recipe, Log
from barcodes.serializers import ItemSerializer, UserSerializer, RecipeSerializer, LogSerializer
from barcodes.permissions import IsOwnerOrReadOnly
from barcodes.api import *

from django.contrib.auth.models import User
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, renderers, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

# Put API lookup here
# make new file 'api.py' -> put all api calls
# import requets for API calls
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/
#

# create item, create recipe, create logs

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class AccountViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing the accounts
#     associated with the user.
#     """
#     serializer_class = UserSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def get_queryset(self):
#         print(self.request.user.accounts.all())
#         return self.request.user.accounts.all()

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

    # def update(self, instance, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #     instance.name = validated_data.get('name', instance.name) # recipe name
    #     ingredients_list = []
    #
    #     for ingredient in ingredients_data:
    #         ingredient, created = Item.objects.get_or_create(name=ingredient["name"])
    #         ingredients_list.append(ingredient)
    #
    #     instance.ingredients = ingredients_list
    #     instance.save()
    #     return instance


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()

def create_recipe(request, format=None):
    req = json.loads(request.data.decode())
    recipe = Recipe(owner=req['owner'], title=req['title'])
    recipe.save()
    for i in req['ingredients']:
        recipe.ingredients.add(Item(**getJSON(i['item'],i['quantity'])))
    recipe.save()
    # return HttpResponse("OK")

    # 'owner': username,
    # 'title': recipe name,
    # 'ingredients': [
    #       {item: food name
    #         quantity: amount}, {}, {}
    # ]

def calc_recipe_nutrition(request, title, username):
    itemdata = ['carbohydrate','fats','protein','calorie','quantity']
    try:
        user = User.objects.filter(username=username)[0]
        recipes = Recipe.objects.get_queryset().filter(owner=user,title=title.replace("%20", " "))[0]
        items = recipes.ingredients.all()

        respData = {}
        for i in items:
            t = model_to_dict(Item(), fields=itemdata)
            t1 = model_to_dict(i, fields=itemdata)
            respData = {k: t.get(k) + t1.get(k) for k in set(t)}
        return JsonResponse(respData)
    except:
        return HttpResponseNotFound(status=404)

def get_recipe(request, title, username):
    try:
        user = User.objects.filter(username=username)[0]
        recipe = Recipe.objects.get_queryset().filter(owner=user,title=title.replace("%20", " "))
        rec_json = serializers.serialize("json", recipe)
        return HttpResponse(rec_json)
    except:
        return HttpResponseNotFound(status=404)

def get_log(request, username):
    try:
        user = User.objects.filter(username=username)[0]
        log = Log.objects.get_queryset().filter(owner=user)
        log_json = serializers.serialize("json", log, fields = ("pk"))
        return HttpResponse(log_json)
    except:
        return HttpResponseNotFound(status=404)

    # filter by name
    # 'owner': username

@csrf_exempt
def create_log(request):
    req = json.loads(request.body.decode())
    log = Log(owner=req['owner'])
    log.save()
    for i in req['items']:
        log.data.add(Item(**getJSON(i['item'],i['quantity'])))
    log.save()

def calc_log_nutrition(request, id, username):
    itemdata = ['carbohydrate','fats','protein','calorie','quantity']
    try:
        user = User.objects.filter(username=username)[0]
        logs = Log.objects.get_queryset().filter(owner=user,id=id)[0]
        items = logs.data.all()

        respData = {}
        for i in items:
            t = model_to_dict(Item(), fields=itemdata)
            t1 = model_to_dict(i, fields=itemdata)
            respData = {k: t.get(k) + t1.get(k) for k in set(t)}
        return JsonResponse(respData)
    except:
        return HttpResponseNotFound(status=404)

    # 'owner': username,
    # 'items': [
    #       {item: food name
            # quantity: amount}, {}, {}
    # ]
