from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(data=product.data, status=status.HTTP_201_CREATED)
        return Response(data=product.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get(self, request, name):
        product = Product.objects.get(name=name)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    def delete(self, request, name):
        product = Product.objects.get(name=name)
        product.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, name):
        product = Product.objects.get(name=name)
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
