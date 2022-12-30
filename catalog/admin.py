from django.contrib import admin
from .models import Catalog


class CatalogAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    list_display = ('id', 'name')

admin.site.register(Catalog, CatalogAdmin)
