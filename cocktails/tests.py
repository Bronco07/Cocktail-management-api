from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Ingredient, Cocktail

class IngredientAPITestCase(APITestCase):
    def setUp(self):
        Ingredient.objects.create(name="Rum", is_alcoholic=True)

    def test_get_ingredients(self):
        response = self.client.get('/api/ingredients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CocktailAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.ingredient = Ingredient.objects.create(name="Limonka", is_alcoholic=False)

    def test_create_cocktail_unauthorized(self):
        data = {
            "name": "Mojito",
            "category": "Klasyczne",
            "instructions": "Wymieszaj składniki.",
            "ingredients_input": [
                {
                    "ingredient": self.ingredient.id,
                    "amount": "2 plasterki"
                }
            ]
        }
        response = self.client.post('/api/cocktails/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_cocktail_authorized(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "Mojito Testowe",
            "category": "Test",
            "instructions": "Wymieszaj i wypij.",
            "ingredients_input": [
                {
                    "ingredient": self.ingredient.id,
                    "amount": "1 sztuka"
                }
            ]
        }
        response = self.client.post('/api/cocktails/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_cocktail_invalid_ingredient_id(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "Invalid Ingredient Cocktail",
            "category": "Test",
            "instructions": "Mix.",
            "ingredients_input": [
                {
                    "ingredient": 99999, 
                    "amount": "50 ml"
                }
            ]
        }
        response = self.client.post('/api/cocktails/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('ingredients_input', response.data)

    def test_update_cocktail_ingredients(self):
        self.client.force_authenticate(user=self.user)
        
        second_ingredient = Ingredient.objects.create(name="Mięta", is_alcoholic=False)
        
        cocktail = Cocktail.objects.create(
            name="Starry Mojito",
            category="Classic",
            instructions="Mix",
            author=self.user
        )
        
        update_data = {
            "name": "Starry Mojito Updated",
            "category": "Classic",
            "instructions": "Mix better",
            "ingredients_input": [
                {
                    "ingredient": second_ingredient.id,
                    "amount": "5 liści"
                }
            ]
        }
        response = self.client.put(f'/api/cocktails/{cocktail.id}/', update_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        from .models import CocktailIngredient
        cocktail_ingredients = CocktailIngredient.objects.filter(cocktail=cocktail)
        
        self.assertEqual(cocktail_ingredients.count(), 1)
        self.assertEqual(cocktail_ingredients.first().ingredient, second_ingredient)