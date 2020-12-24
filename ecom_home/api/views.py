# decoretors
from django.contrib.auth.decorators import login_required
from rest_framework import status 
from rest_framework.response import Response  
from rest_framework.decorators import api_view
# serializer
from ecom_home.api.serializers import ItemSerializer , Item1Serializer,Item2Serializer,CATEGORYSerializer,BannerSerializer,Banner2Serializer,Deals_of_the_day_Serializer
# models
from ecom_home.models import Item, OrderItem, Order, Address ,Item_by_seller,SellerAccount_requested , CATEGORY,cal_cat,seller_address,SUB_CATEGORY,SUB_CATEGORY_Type,SHIPPING_MODE,ORDERS,Banner,Banner2
@api_view([ 'GET'])
def ORDER(request ):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        items = ORDERS.objects.all()
        serializer = ItemSerializer(items, many=True)
        # print(serializer)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

@api_view([ 'GET'])
def Deals_of_the_day_api(request):
    if request.method == 'GET':

        item2 = Item.objects.filter(Deals_of_the_day = True)
        serializer = Deals_of_the_day_Serializer(item2, many = True )
        return Response(serializer.data)

@api_view([ 'GET'])
def Item_api(request , slug ):
    if request.method == 'GET':
        item1 = Item.objects.get(slug = slug)
        serializer = Item1Serializer(item1 )
        return Response(serializer.data)



@api_view([ 'GET'])
def Items_api(request ):
    if request.method == 'GET':
        item2 = Item.objects.all()
        serializer = Item2Serializer(item2, many = True )
        return Response(serializer.data)
        
@api_view([ 'GET'])
@login_required
def Category_api(request):
    if request.method == 'GET' :
        cateory = CATEGORY.objects.all()
        serializer = CATEGORYSerializer(cateory, many= True)
        return Response(serializer.data)     

# banner          
@api_view([ 'GET'])

def Banner_api(request):
    if request.method == 'GET' :
        banner = Banner.objects.all()
        serializer = BannerSerializer(banner, many= True)
        return Response(serializer.data)    


@api_view([ 'GET'])
def Banner2_api(request):
    if request.method == 'GET' :
        banner = Banner2.objects.all()
        serializer = Banner2Serializer(banner, many= True)
        return Response(serializer.data)       