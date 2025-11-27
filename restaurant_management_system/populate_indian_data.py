import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management_system.settings')
django.setup()

from menu.models import Category, Item, Recipe
from inventory.models import InventoryItem

def populate():
    print("Populating data...")

    # 1. Create Categories
    categories = {
        'Starters': Category.objects.get_or_create(name='Starters')[0],
        'Main Course': Category.objects.get_or_create(name='Main Course')[0],
        'Breads': Category.objects.get_or_create(name='Breads')[0],
        'Rice': Category.objects.get_or_create(name='Rice')[0],
        'Beverages': Category.objects.get_or_create(name='Beverages')[0],
    }

    # 2. Create Inventory Items (Ingredients)
    inventory = {
        'Chicken': InventoryItem.objects.get_or_create(name='Chicken', defaults={'quantity': 50, 'unit': 'kg'})[0],
        'Paneer': InventoryItem.objects.get_or_create(name='Paneer', defaults={'quantity': 30, 'unit': 'kg'})[0],
        'Basmati Rice': InventoryItem.objects.get_or_create(name='Basmati Rice', defaults={'quantity': 100, 'unit': 'kg'})[0],
        'Spices': InventoryItem.objects.get_or_create(name='Spices', defaults={'quantity': 20, 'unit': 'kg'})[0],
        'Flour (Atta)': InventoryItem.objects.get_or_create(name='Flour (Atta)', defaults={'quantity': 50, 'unit': 'kg'})[0],
        'Butter': InventoryItem.objects.get_or_create(name='Butter', defaults={'quantity': 20, 'unit': 'kg'})[0],
        'Onions': InventoryItem.objects.get_or_create(name='Onions', defaults={'quantity': 40, 'unit': 'kg'})[0],
        'Tomatoes': InventoryItem.objects.get_or_create(name='Tomatoes', defaults={'quantity': 30, 'unit': 'kg'})[0],
        'Yogurt': InventoryItem.objects.get_or_create(name='Yogurt', defaults={'quantity': 20, 'unit': 'kg'})[0],
    }

    # 3. Create Menu Items
    menu_items = [
        {
            'name': 'Butter Chicken',
            'category': categories['Main Course'],
            'price': 350.00,
            'description': 'Tender chicken cooked in a rich tomato and butter gravy.',
            'ingredients': [
                ('Chicken', 0.3),
                ('Butter', 0.05),
                ('Tomatoes', 0.2),
                ('Spices', 0.02),
            ]
        },
        {
            'name': 'Paneer Tikka Masala',
            'category': categories['Main Course'],
            'price': 320.00,
            'description': 'Grilled paneer cubes in a spicy curry sauce.',
            'ingredients': [
                ('Paneer', 0.25),
                ('Onions', 0.1),
                ('Tomatoes', 0.15),
                ('Spices', 0.03),
            ]
        },
        {
            'name': 'Chicken Biryani',
            'category': categories['Rice'],
            'price': 280.00,
            'description': 'Aromatic basmati rice cooked with spices and chicken.',
            'ingredients': [
                ('Chicken', 0.2),
                ('Basmati Rice', 0.25),
                ('Spices', 0.05),
                ('Onions', 0.1),
            ]
        },
        {
            'name': 'Butter Naan',
            'category': categories['Breads'],
            'price': 40.00,
            'description': 'Soft indian bread topped with butter.',
            'ingredients': [
                ('Flour (Atta)', 0.15),
                ('Butter', 0.01),
            ]
        },
        {
            'name': 'Mango Lassi',
            'category': categories['Beverages'],
            'price': 80.00,
            'description': 'Refreshing yogurt-based mango drink.',
            'ingredients': [
                ('Yogurt', 0.2),
            ]
        }
    ]

    # 4. Create Items and Recipes
    for m_item in menu_items:
        item, created = Item.objects.get_or_create(
            name=m_item['name'],
            defaults={
                'category': m_item['category'],
                'price': m_item['price'],
                'description': m_item['description']
            }
        )
        
        if created:
            print(f"Created Menu Item: {item.name}")
        else:
            print(f"Updated Menu Item: {item.name}")
            item.price = m_item['price']
            item.description = m_item['description']
            item.save()

        # Create Recipes
        # First, clear existing recipes to avoid duplicates if re-running
        item.recipes.all().delete()
        
        for ing_name, qty in m_item['ingredients']:
            inv_item = inventory[ing_name]
            Recipe.objects.create(
                menu_item=item,
                inventory_item=inv_item,
                quantity_required=qty
            )
            print(f"  - Linked {qty} {inv_item.unit} of {ing_name}")

    print("Data population complete!")

if __name__ == '__main__':
    populate()
