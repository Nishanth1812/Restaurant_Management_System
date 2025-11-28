import os
import django
import sys

# Setup Django environment
sys.path.append(r'c:\Users\Devab\OneDrive\Desktop\College\S3\Intro to Python\Restaurant_Management_System\restaurant_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management_system.settings')
django.setup()

from menu.models import Item, Category, Recipe
from inventory.models import InventoryItem
from menu.serializers import ItemSerializer

def verify_ingredients():
    print("Starting verification...")

    # 1. Setup Data
    category, _ = Category.objects.get_or_create(name="Test Category")
    inv_item, _ = InventoryItem.objects.get_or_create(name="Test Ingredient", defaults={'quantity': 100, 'unit': 'kg'})
    
    print(f"Created/Found Category: {category.name}")
    print(f"Created/Found Inventory Item: {inv_item.name} (ID: {inv_item.id})")

    # 2. Test Create with Ingredients
    item_data = {
        'name': 'Test Menu Item',
        'description': 'Test Description',
        'price': 10.00,
        'category': category.id,
        'recipes': [
            {'inventory_item_id': inv_item.id, 'quantity_required': 0.5}
        ]
    }

    serializer = ItemSerializer(data=item_data)
    if serializer.is_valid():
        item = serializer.save()
        print(f"Created Item: {item.name} (ID: {item.id})")
    else:
        print("Create Validation Failed:", serializer.errors)
        return

    # Verify Recipe
    recipe = Recipe.objects.filter(menu_item=item).first()
    if recipe and recipe.inventory_item == inv_item and recipe.quantity_required == 0.5:
        print("SUCCESS: Recipe created correctly.")
    else:
        print("FAILURE: Recipe not created correctly.")
        if recipe:
            print(f"Actual: {recipe.inventory_item.name}, {recipe.quantity_required}")
        else:
            print("No recipe found.")

    # 3. Test Update with Ingredients
    update_data = {
        'name': 'Test Menu Item Updated',
        'description': 'Test Description',
        'price': 12.00,
        'category': category.id,
        'recipes': [
            {'inventory_item_id': inv_item.id, 'quantity_required': 1.5}
        ]
    }

    serializer = ItemSerializer(item, data=update_data)
    if serializer.is_valid():
        item = serializer.save()
        print(f"Updated Item: {item.name}")
    else:
        print("Update Validation Failed:", serializer.errors)
        return

    # Verify Update
    recipe = Recipe.objects.filter(menu_item=item).first()
    if recipe and recipe.quantity_required == 1.5:
        print("SUCCESS: Recipe updated correctly.")
    else:
        print("FAILURE: Recipe not updated correctly.")
        if recipe:
            print(f"Actual: {recipe.quantity_required}")

    # Cleanup
    item.delete()
    # inv_item.delete() # Keep inventory item for manual testing if needed
    # category.delete()
    print("Cleanup done.")

if __name__ == "__main__":
    verify_ingredients()
