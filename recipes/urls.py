from django.urls import path
from recipes.views import *


app_name = 'recipes'

urlpatterns = [
    path('', home_view, name='home'),
    path('receitas/<int:recipe_id>/', recipes_view, name='recipe'),
    path('receitas/categoria/<int:category_id>/', category_view, name='category')
]


