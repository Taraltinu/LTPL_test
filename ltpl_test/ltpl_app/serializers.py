from rest_framework import serializers
from ltpl_app.models import Product ,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ["order_no","product"]