from django.db.migrations import serializer
from rest_framework import viewsets
from .models import Ingredient, Cocktail
from .serializers import IngredientSerializer, CocktailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    filterset_fields = ['is_alcoholic']

    search_fields = ['name', 'description']

    ordering_fields = ['name', 'id']


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    filterset_fields = ['category', 'ingredients']

    search_fields = ['name', 'instructions', 'ingredients__name']

    ordering_fields = ['name', 'created_at']

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)