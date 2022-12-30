from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'username', 'phone_number')
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'money', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)
