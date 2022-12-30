from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Favorites
from .serializers import FavoritesSerializer

class FavoritesView(APIView):
    def get(self, request):
        user_id = request.user.id
        favorites = Favorites.objects.filter(user_id=user_id)
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritesDetailView(APIView):
    def get(self, request, id):
        favorites = Favorites.objects.get(id=id)
        serializer = FavoritesSerializer(favorites)
        return Response(data=serializer.data)

    def delete(self, request, id):
        favorites = Favorites.objects.get(id=id)
        if request.user.id == favorites.user.id:
            favorites.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
