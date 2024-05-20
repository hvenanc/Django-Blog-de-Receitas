from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home_view),
    path('receitas/<int:id>/', recipes_view),
]


