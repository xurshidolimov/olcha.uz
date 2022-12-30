from django.contrib import admin
from cart.models import Cart

class CartAdmin(admin.ModelAdmin):
    search_fields = ('id', )
    list_display = ('id', 'user', 'product', 'paid')
    list_filter = ('user', 'product')

admin.site.register(Cart, CartAdmin)
