from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer

# Create your views here.
class productListAPIView(APIView):
    def get(self, request):
        all_products = Product.objects.all()
        
        serializer = ProductSerializer(all_products, many=True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class productDetailAPIViw(APIView):
    def get(self, request, pk):
        all_product = Product.objects.all(pk)
        serializer = ProductSerializer(all_product, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

