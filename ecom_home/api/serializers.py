
from rest_framework import serializers
from ecom_home.models import Item, OrderItem, Order, Address ,Item_by_seller,SellerAccount_requested , CATEGORY,cal_cat,seller_address,SUB_CATEGORY,SUB_CATEGORY_Type,SHIPPING_MODE,ORDERS,Banner,Banner2


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORDERS
        fields = ['seller', 'quantity', 'date', 'item' ]


class Item1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['seller' , 'slug', 'title']

class Deals_of_the_day_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['seller' , 'slug', 'title' , 'image' , 'Deals_of_the_day']
class Item2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['seller' , 'slug', 'title' ]


class CATEGORYSerializer(serializers.ModelSerializer):
    class Meta:
        model = CATEGORY
        fields = ['Category' , 'Image']
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['link' , 'color']
    
            

class Banner2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Banner2
        fields = ['link' , 'color']