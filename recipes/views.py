from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe


def home_view(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)],
    })


def recipes_view(request, id):
    return HttpResponse(render(request, 'recipes/pages/recipe-detail.html', context= {
        'recipe': make_recipe(),
        'is_detail_page': True
    }))






