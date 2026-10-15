from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nazwa")
    description = models.TextField(blank=True, verbose_name="Opis")
    is_alcoholic = models.BooleanField(default=False, verbose_name="Czy alkoholowy")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL do zdjęcia")

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nazwa koktajlu")
    category = models.CharField(max_length=50, verbose_name="Kategoria")
    instructions = models.TextField(verbose_name="Instrukcja przygotowania")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cocktails', verbose_name="Autor", blank=True, null=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='CocktailIngredient',
        related_name='cocktails',
        verbose_name="Składniki",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='cocktail_recipes')
    amount = models.CharField(max_length=50, verbose_name="Ilość/Proporcja") 

    class Meta:
        unique_together = ('cocktail', 'ingredient')

    def __str__(self):
        return f"{self.amount} - {self.ingredient.name} w {self.cocktail.name}"