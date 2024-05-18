from django.urls import path
from recipes.views import home_view, sobre_view

urlpatterns = [
    path('', home_view),
    path('sobre', sobre_view),
]


