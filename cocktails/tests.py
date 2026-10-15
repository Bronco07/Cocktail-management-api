from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Ingredient
from django.contrib.auth.models import User
from .models import Cocktail

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
            "ingredients": [
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
                {"ingredient_id": self.ingredient.id, "amount": "1 sztuka"}
            ]
        }
        response = self.client.post('/api/cocktails/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


