from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(data=category.data, status=status.HTTP_201_CREATED)
        return Response(data=category.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get(self, request, name):
        category = Category.objects.get(name=name)
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)

    def delete(self, request, name):
        category = Category.objects.get(name=name)
        category.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, name):
        category = Category.objects.get(name=name)
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

