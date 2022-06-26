from rest_framework import serializers
from sales.models import Product ,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    user_name = serializers.CharField(source="user.name")
    total_quantity = serializers.IntegerField(read_only=True)
    total_price = serializers.DecimalField(read_only=True,max_digits=12,decimal_places=3)

    class Meta:
        model = Order
        fields = ["order_no","user_name","ordered_on","total_quantity","total_price","is_placed","product"]