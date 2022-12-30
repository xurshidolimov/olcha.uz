from django.urls import path
from .views import ProductView, ProductDetailView


urlpatterns = [
    path('', ProductView.as_view()),
    path('<str:name>/', ProductDetailView.as_view()),
]