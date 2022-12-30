from catalog.serializers import CatalogSerializer
from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(read_only=True)
    catalog_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'catalog', 'catalog_id')


