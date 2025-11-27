from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    # inventory_item field is removed in favor of Recipe model for multi-ingredient support

    def __str__(self):
        return self.name

class Recipe(models.Model):
    menu_item = models.ForeignKey(Item, related_name='recipes', on_delete=models.CASCADE)
    inventory_item = models.ForeignKey('inventory.InventoryItem', related_name='used_in', on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity required per unit of menu item")

    def __str__(self):
        return f"{self.menu_item.name} requires {self.quantity_required} of {self.inventory_item.name}"
