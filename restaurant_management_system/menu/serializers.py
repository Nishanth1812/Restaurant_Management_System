from rest_framework import serializers
from .models import Category, Item, Recipe

class RecipeSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='inventory_item.name')
    unit = serializers.ReadOnlyField(source='inventory_item.unit')
    inventory_item_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'inventory_item_id', 'ingredient_name', 'quantity_required', 'unit']

class ItemSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'is_available', 'category', 'recipes']

    def create(self, validated_data):
        recipes_data = validated_data.pop('recipes', [])
        item = Item.objects.create(**validated_data)
        for recipe_data in recipes_data:
            Recipe.objects.create(menu_item=item, **recipe_data)
        return item

    def update(self, instance, validated_data):
        recipes_data = validated_data.pop('recipes', None)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        if recipes_data is not None:
            instance.recipes.all().delete()
            for recipe_data in recipes_data:
                Recipe.objects.create(menu_item=instance, **recipe_data)
        
        return instance

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'items']
