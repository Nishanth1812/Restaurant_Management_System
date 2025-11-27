from django.db import transaction
from rest_framework import viewsets, permissions
from .models import Order, Table
from .serializers import OrderSerializer, TableSerializer
from accounts.permissions import IsAdmin

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated] # We might want to restrict delete to Admin later, but for now user asked for Admin to remove.
    # Actually, let's make it so only Admin can delete.
    # But wait, IsAuthenticated allows anyone to delete? Yes.
    # Let's import IsAdminOrReadOnly and use it? 
    # Or better, create a custom permission IsAdminOrCreateOnly?
    # For now, let's stick to IsAuthenticated but handle UI hiding. 
    # The user said "admin should be able to remove", implying staff shouldn't?
    # Let's use IsAdminOrReadOnly for OrderViewSet too? No, staff needs to create orders.
    # Let's leave it as IsAuthenticated for now to avoid breaking Staff order creation, 
    # but I will add a check in destroy method or just rely on UI for now as per "admin should be able to remove"
    # Actually, let's add a custom permission or just override get_permissions.
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAuthenticated(), IsAdmin()]
        return [permissions.IsAuthenticated()]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
