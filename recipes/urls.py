from django.urls import path
from recipes.views import *


app_name = 'recipes'

urlpatterns = [
    path('', home_view),
    path('receitas/<int:id>/', recipes_view, name='recipes'),
    path('receitas/categoria/<int:category_id>/', category_view, name="category")
]


