from django.contrib import admin
from django.urls import path, include
from .views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view()),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('favorites/', include('favorites.urls')),
]
