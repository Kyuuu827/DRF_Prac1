from rest_framework          import viewsets
from rest_framework.views    import APIView
from rest_framework.response import Response

from .serializers   import ProductSerializer
from .models        import Product


class ProductView(APIView):
    def get(self, request, format=None):
        productlist = Product.objects.all()
        serializer = ProductSerializer(productlist, many=True) # many=True는 Json을 리스트형태로 받는 것
        return Response(serializer.data)