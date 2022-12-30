from rest_framework import serializers
from .models import Favorites
from users.serializers import CustomUserSerializer
from product.serializers import ProductSerializer


class FavoritesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    product_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Favorites
        fields = ('id', 'user', 'product', 'user_id', 'product_id')
