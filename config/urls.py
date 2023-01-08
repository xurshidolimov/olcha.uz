from django.contrib import admin
from django.urls import path, include
from .views import LandingPage
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='olch.uz',
        description='olcha.uz clone',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='xurshidolimov017@gmail.com'),
        license=openapi.License(name="olcha.uz license")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', LandingPage.as_view()),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('favorites/', include('favorites.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
