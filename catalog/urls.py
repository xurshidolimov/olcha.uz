from django.urls import path
from .views import CatalogView, CatalogDetailView


urlpatterns = [
    path('', CatalogView.as_view()),
    path('<str:name>/', CatalogDetailView.as_view()),
]
