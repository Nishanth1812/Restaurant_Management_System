import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_mgmt.settings')
django.setup()

from menu.models import Category
from inventory.models import InventoryItem
from orders.models import Table

def seed():
    # Categories
    categories = ['Appetizers', 'Main Course', 'Desserts', 'Beverages']
    for name in categories:
        Category.objects.get_or_create(name=name)
    print(f"Seeded {len(categories)} categories.")

    # Inventory
    inventory_items = [
        {'name': 'Tomatoes', 'quantity': 50, 'unit': 'kg', 'low_stock_threshold': 5},
        {'name': 'Cheese', 'quantity': 20, 'unit': 'kg', 'low_stock_threshold': 2},
        {'name': 'Chicken', 'quantity': 30, 'unit': 'kg', 'low_stock_threshold': 5},
        {'name': 'Rice', 'quantity': 100, 'unit': 'kg', 'low_stock_threshold': 10},
        {'name': 'Soda Cans', 'quantity': 200, 'unit': 'cans', 'low_stock_threshold': 20},
    ]
    for item in inventory_items:
        InventoryItem.objects.get_or_create(name=item['name'], defaults=item)
    print(f"Seeded {len(inventory_items)} inventory items.")

    # Tables
    tables = [
        {'number': 1, 'capacity': 4},
        {'number': 2, 'capacity': 2},
        {'number': 3, 'capacity': 6},
        {'number': 4, 'capacity': 4},
        {'number': 5, 'capacity': 8},
    ]
    for table in tables:
        Table.objects.get_or_create(number=table['number'], defaults=table)
    print(f"Seeded {len(tables)} tables.")

if __name__ == '__main__':
    seed()
