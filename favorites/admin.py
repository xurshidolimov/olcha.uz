from django.contrib import admin
from .models import Favorites

class FavoritesAdmin(admin.ModelAdmin):
    search_fields = ('id', )
    list_display = ('id', 'user', 'product')

admin.site.register(Favorites, FavoritesAdmin)
