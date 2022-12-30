from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    list_display = ('id', 'name', 'price', 'category', 'image')

admin.site.register(Product, ProductAdmin)
