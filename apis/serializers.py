from rest_framework import serializers

from watch.models import Order,Product,Discount

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("__all__")



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")        

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ("__all__")    