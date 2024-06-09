from django.shortcuts import render
from django.http import HttpResponse, Http404
from recipes.models import Recipe
from django.contrib import messages
from django.db.models import Q
from utils.pagination import make_pagination


def home_view(request):

    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    recipes_for_page, pagination_range = make_pagination(request, recipes, 3)

    messages.success(request, 'Bem-vindo')
    messages.error(request, 'Bem-vindo')
    messages.warning(request, 'Bem-vindo')
    messages.info(request, 'Bem-vindo')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes_for_page,
        'pagination_range': pagination_range, 
    })


def category_view(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    recipes_for_page, pagination_range = make_pagination(request, recipes, 3)

    if not recipes:
        raise Http404('Category Not Found')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes_for_page,
        'pagination_range': pagination_range,
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

    recipes_for_page, pagination_range = make_pagination(request, recipes, 3)
    
    return render(request, 'recipes/pages/search.html', {
        'recipes': recipes_for_page,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })



