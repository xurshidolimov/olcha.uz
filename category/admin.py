from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    list_display = ('id', 'name', 'catalog')

admin.site.register(Category, CategoryAdmin)
