from django.urls import path
from recipes.views import *


app_name = 'recipes'

urlpatterns = [
    path('', home_view),
    path('receitas/<int:recipe_id>/', recipes_view, name='recipe'),
    path('receitas/categoria/<int:category_id>/', category_view, name="category")
]


