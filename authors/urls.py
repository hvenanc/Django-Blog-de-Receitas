from django.urls import path
from authors import views


app_name = 'authors'

urlpatterns = [
    path('registro/', views.register_view, name='register'),
    path('registro/criar/', views.register_create, name='create'),
    path('login/', views.login_view, name='login'),
    path('login/sucesso/', views.login_success , name='login_success'),
    path('home/', views.home_view, name='home'),
    path('sair/', views.logout_view, name='logout')
]

