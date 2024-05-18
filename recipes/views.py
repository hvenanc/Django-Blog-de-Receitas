from django.shortcuts import render
from django.http import HttpResponse


def sobre_view(request):
    return HttpResponse('<h1>Minha Pagina Sobre</h1>')


def home_view(request):
    return render(request, 'recipes/pages/home.html')



