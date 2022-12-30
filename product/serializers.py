from rest_framework import serializers
from product.models import Product
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'category_id', 'price', 'image', 'description',
                  'create_at', 'memory', 'ram', 'camera1', 'camera2', 'battery', 'fingerprint',
                  'face_unlock', 'processor', 'country', 'company', 'size', 'weight', 'sim',
                  'colors', 'electr', 'volume', 'max_weight', 'speed', 'display', 'wifi')
