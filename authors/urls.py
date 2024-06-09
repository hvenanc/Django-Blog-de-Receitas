from django.urls import path
from authors import views

urlpatterns = [
    path('registro/', views.register_view, name='register'),
]

