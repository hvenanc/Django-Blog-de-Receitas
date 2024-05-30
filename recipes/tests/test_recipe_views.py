from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):


    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home_view)


    def test_recipe_category_view_function_is_correct(self):
        view =  resolve(
            reverse('recipes:category', kwargs={'category_id' : 1})
            )
        self.assertIs(view.func, views.category_view)

    
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'recipe_id': 1})
        )
        self.assertIs(view.func, views.recipes_view)