from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Cart
from users.serializers import CustomUserSerializer


class CartSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'user_id', 'product_id', 'paid')
