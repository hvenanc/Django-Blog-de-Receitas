from django.urls import path
from authors import views


app_name = 'authors'

urlpatterns = [
    path('registro/', views.register_view, name='register'),
    path('registro/criar/', views.register_create, name='create')
]

