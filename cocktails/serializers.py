from rest_framework import serializers
from .models import Ingredient, Cocktail, CocktailIngredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description', 'is_alcoholic', 'image_url']


class CocktailIngredientReadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    is_alcoholic = serializers.ReadOnlyField(source='ingredient.is_alcoholic')

    class Meta:
        model = CocktailIngredient
        fields = ['id', 'name', 'amount', 'is_alcoholic']


class CocktailIngredientWriteSerializer(serializers.Serializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    amount = serializers.CharField(max_length=50)


class CocktailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    ingredients = CocktailIngredientReadSerializer(
        source='recipe_ingredients', 
        many=True, 
        read_only=True
    )
    
    ingredients_input = CocktailIngredientWriteSerializer(
        many=True, 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Cocktail
        fields = [
            'id', 'name', 'category', 'instructions', 
            'author', 'ingredients', 'ingredients_input', 'created_at'
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients_input', [])
        
        cocktail = Cocktail.objects.create(**validated_data)

        for item in ingredients_data:
            CocktailIngredient.objects.create(
                cocktail=cocktail,
                ingredient=item['ingredient'], 
                amount=item['amount']
            )

        return cocktail

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients_input', None)

        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.save()

        if ingredients_data is not None:
            instance.recipe_ingredients.all().delete()
            for item in ingredients_data:
                CocktailIngredient.objects.create(
                    cocktail=instance,
                    ingredient=item['ingredient'],
                    amount=item['amount']
                )

        return instance