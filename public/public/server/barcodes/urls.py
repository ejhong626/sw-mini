from django.urls import path, include
from rest_framework.routers import DefaultRouter
from barcodes import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recipe', views.RecipeViewSet)
router.register(r'log', views.LogViewSet)
router.register(r'item', views.ItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('<str:username>/<str:title>/reccalculate/',views.calc_recipe_nutrition),
    path('<str:username>/<int:id>/logcalculate/',views.calc_log_nutrition)
]

urlpatterns += router.urls
# /users/<int:id>/
# /users/<int:id>/
