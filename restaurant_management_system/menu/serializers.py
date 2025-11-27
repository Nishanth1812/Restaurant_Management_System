from rest_framework import serializers
from .models import Category, Item, Recipe

class RecipeSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='inventory_item.name')
    unit = serializers.ReadOnlyField(source='inventory_item.unit')

    class Meta:
        model = Recipe
        fields = ['ingredient_name', 'quantity_required', 'unit']

class ItemSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'is_available', 'category', 'recipes']

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'items']
