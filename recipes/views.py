from django.shortcuts import render
from django.http import HttpResponse, Http404
from recipes.models import Recipe
from django.db.models import Q


def home_view(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category_view(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Category Not Found')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipes_view(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id, is_published=True).order_by('-id').first()
    return HttpResponse(render(request, 'recipes/pages/recipe-detail.html', context= {
        'recipe': recipe,
        'is_detail_page': True
    }))


def search_view(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404('Termo Inválido!')
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    
    return render(request, 'recipes/pages/search.html', {
        'recipes': recipes
    })



