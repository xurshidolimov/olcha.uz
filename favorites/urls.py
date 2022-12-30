from .views import FavoritesView, FavoritesDetailView
from django.urls import path


urlpatterns = [
    path('', FavoritesView.as_view()),
    path('<int:id>/', FavoritesDetailView.as_view()),
]
