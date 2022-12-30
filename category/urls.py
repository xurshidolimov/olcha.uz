from django.urls import path
from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('<str:name>/', CategoryDetailView.as_view()),
]
