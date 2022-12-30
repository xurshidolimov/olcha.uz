from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart
from catalog.models import Catalog
from catalog.serializers import CatalogSerializer
from category.models import Category
from category.serializers import CategorySerializer
from favorites.models import Favorites
from product.models import Product
from product.serializers import ProductSerializer


class LandingPage(APIView):
    def get(self, request):
        def determiner(carts):
            categorys_interest_list = []
            for cart in carts:
                product = Product.objects.get(id=cart.product_id)
                obj = Category.objects.get(id=product.category_id)
                if obj not in categorys_interest_list:
                    categorys_interest_list.append(obj)
            return CategorySerializer(categorys_interest_list[-3:], many=True)

        #all catalogs   # barcha cataloglar
        catalog = Catalog.objects.all()
        catalog_ser = CatalogSerializer(catalog, many=True)

        #all categorys   # barcha categorylar
        category = Category.objects.all()
        category_ser = CategorySerializer(category, many=True)

        # the category in which the user has purchased the most products
        user_purchased = determiner(Cart.objects.filter(user_id=request.user.id))

        # the category of most interest to the user
        user_interested = determiner(Favorites.objects.filter(user_id=request.user.id))

        # the category that everyone buys the most products from
        everyone_purchased = determiner(Cart.objects.all())

        # the category that everyone is most interested in
        everyone_interested = determiner(Favorites.objects.all())

        # all Product
        product = Product.objects.all().order_by('id')
        serializer = ProductSerializer(product, many=True)

        return Response(data=[
            catalog_ser.data,
            category_ser.data,
            user_purchased.data,
            user_interested.data,
            everyone_purchased.data,
            everyone_interested.data,
            serializer.data
        ])
