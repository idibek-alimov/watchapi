from django.shortcuts import render
from rest_framework import generics
from watch.models import Order,Product,Discount
from .serializers import OrderSerializer,ProductSerializer,DiscountSerializer

############## ORDER #######################
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



################### DISCOUNT #################
class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    def create(self, request, *args, **kwargs):
        print("Sike")


##################### PRODUCT #################
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
