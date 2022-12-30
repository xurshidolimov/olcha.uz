from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CartView(APIView):
    def get(self, request):
        user_id = request.user.id
        cart = Cart.objects.filter(user_id=user_id)
        serializer = CartSerializer(cart, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailView(APIView):
    def get(self, request, id):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart)
        return Response(data=serializer.data)

    def delete(self, request, id):
        cart = Cart.objects.get(id=id)
        if request.user.id == cart.user_id:
            cart.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(instance=cart, data=request.data, partial=True)
        if serializer.is_valid() and cart.user_id == request.user.id:
            print(4)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
