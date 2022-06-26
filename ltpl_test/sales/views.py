from rest_framework import viewsets
from sales.models import Product,Order
from sales.serializers import ProductSerializer,OrderSerializer
from django.db.models import Sum,Count,F

class ProductView(viewsets.ModelViewSet):
    queryset = (Product.objects.all())
    serializer_class = ProductSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = (Order.objects.annotate(
        total_price = Sum("product__price"),
        total_quantity = Count("product__quantity"),

    )
    .distinct())
    serializer_class = OrderSerializer
        