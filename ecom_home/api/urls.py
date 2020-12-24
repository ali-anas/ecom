from django.contrib import admin
from django.urls import path
from ecom_home import views
from .views import*

app_name = 'ecom_home'
urlpatterns = [

    path('item/' , ORDER , name= 'item'),
    path('Deals_of_the_day/' , Deals_of_the_day_api , name= 'Deals_of_the_day'),
    path('product/<slug>/' , Item_api , name= 'Item_api'),
    path('items/' , Items_api , name= 'Items_api'), 
    path('category/' , Category_api , name= 'category'),
    path('banner/' , Banner_api , name= 'banner'),
    path('banner2/' , Banner2_api , name= 'banner2'),
]