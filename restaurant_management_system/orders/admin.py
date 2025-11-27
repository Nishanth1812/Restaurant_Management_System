from django.contrib import admin
from .models import Order, OrderItem, Table

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'status', 'total_price', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Table)
