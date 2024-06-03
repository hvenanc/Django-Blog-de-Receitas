from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')


    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id' : 1})
        self.assertEqual(url, '/receitas/categoria/1/')


    def test_recipe_details_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'recipe_id': 1})
        self.assertEqual(url, '/receitas/1/')

    
    def test_recipe_search_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/receitas/search')