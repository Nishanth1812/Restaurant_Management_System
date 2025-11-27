from rest_framework import serializers
from .models import Order, OrderItem, Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'quantity', 'subtotal']
        read_only_fields = ['subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'created_at', 'total_price', 'items']
        read_only_fields = ['total_price', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        # Check inventory first
        for item_data in items_data:
            menu_item = item_data['item']
            quantity = item_data['quantity']
            
            # Check recipes for this item
            for recipe in menu_item.recipes.all():
                required_amount = recipe.quantity_required * quantity
                if recipe.inventory_item.quantity < required_amount:
                    raise serializers.ValidationError(
                        f"Insufficient stock for {menu_item.name}. "
                        f"Requires {required_amount} {recipe.inventory_item.unit} of {recipe.inventory_item.name}, "
                        f"but only {recipe.inventory_item.quantity} available."
                    )

        # Deduct inventory and create order
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            menu_item = item_data['item']
            quantity = item_data['quantity']
            
            # Deduct from inventory
            for recipe in menu_item.recipes.all():
                inventory_item = recipe.inventory_item
                required_amount = recipe.quantity_required * quantity
                inventory_item.quantity -= required_amount
                inventory_item.save()
                
            OrderItem.objects.create(order=order, **item_data)
        return order
