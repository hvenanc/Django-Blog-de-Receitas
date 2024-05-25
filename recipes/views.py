from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe
from utils.recipes.factory import make_recipe


def home_view(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category_view(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipes_view(request, id):
    return HttpResponse(render(request, 'recipes/pages/recipe-detail.html', context= {
        'recipe': make_recipe(),
        'is_detail_page': True
    }))






