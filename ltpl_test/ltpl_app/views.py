from rest_framework import viewsets
from ltpl_app.models import Product,Order
from ltpl_app.serializers import ProductSerializer,OrderSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = (Product.objects.all())
    serializer_class = ProductSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = (Order.objects.all())
    serializer_class = OrderSerializer