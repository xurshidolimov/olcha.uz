from .models import Catalog
from .serializers import CatalogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CatalogView(APIView):
    def get(self, request):
        catalogs = Catalog.objects.all()
        seriallizer = CatalogSerializer(catalogs, many=True)
        return Response(data=seriallizer.data)

    def post(self, request):
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatalogDetailView(APIView):
    def get(self, request, name):
        catalogs = Catalog.objects.get(name=name)
        seriallizer = CatalogSerializer(catalogs)
        return Response(data=seriallizer.data)

    def delete(self, request, name):
        catalog = Catalog.objects.get(name=name)
        catalog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, name):
        catalog = Catalog.objects.get(name=name)
        serializer = CatalogSerializer(instance=catalog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
