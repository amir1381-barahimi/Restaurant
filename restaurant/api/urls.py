from django.contrib import admin
from django.urls import path , include
from .views import *

app_name = "api"


urlpatterns = [
    
    path("restaurants/",RestaurantListAll.as_view(),name='restaurantAll'), 
    path("restaurants/freeDelivery",RestaurantFreeDelivery.as_view(),name='restaurantFreeDelivery'), 
    path("restaurants/popular",RestaurantPopularList.as_view(),name='popularRestaurant'), 
    path("restaurants/nearest",RestaurantNearest.as_view(),name='nearestRestaurant'), 


    # path("foods/<str:name>",FoodNameDetail.as_view(),name='foodNameDetail'),
    path("foods/",FoodListAll.as_view(),name='foodAll'),
    path("foods/<int:pk>",FoodPKDetail.as_view(),name='foodPKDetail'),
    path("foods/popular",FoodPopularList.as_view(),name='foodPopular'),
    path("foods/fastfood",FoodfastFoodList.as_view(),name='Foodfastfood'),
    path("foods/traditional",FoodTraditionalFoodList.as_view(),name='FoodTraditional'),
    path("foods/foreignfood",FoodForeignFoodList.as_view(),name='FoodForeignfood'),
    
    
    path("users/<int:pk>/update",UserUpdateProfile.as_view(),name='UserUpdate'),
    path("users/",MyUserListAll.as_view(),name='MyUserList'),
    path("users/<int:pk>",MyUserDetail.as_view(),name='MyUserDetail'),
    path("users/<int:pk>/foodFavorite",MyUserFoodLikeDetail.as_view(),name='MyUserFoodLikeDetail'),
    path("users/<int:pk>/restaurantFavorite",MyUserRestaurantLikeDetail.as_view(),name='MyUserFoodLikeDetail'),
    # path("users/restaurantFavorite",MyUserRestaurantLikeDetail.as_view(),name='MyUserFoodLikeDetail'),
    path("users/foodFavorite/add",MyUserFoodLikeAdd.as_view(),name='MyUserFoodLikeAdd'),
    path("users/restaurantFavorite/add",MyUserRestaurantLikeAdd.as_view(),name='MyUserRestaurantLikeAdd'),
    path("users/<int:pk>/Address",AddressUserList.as_view(),name='UserAddressList'),
    path("users/Address/add",UserAddressAdd.as_view(),name='UserAddressAdd'),

    # path("users/<int:pk>",MyUserDetail.as_view(),name='MyUserDetail'),
    
    path("carts/create",CartCreate.as_view(),name='CartCreate'),
    path("carts/",CartListAll.as_view(),name='CartListAll'),
    path("carts/<int:pk>",CartDetail.as_view(),name='cartDetail'),
    path("carts/add",CartAddFood.as_view(),name='CartAddFood'),
    path("carts/<int:pk>/food/",CartFoodList.as_view(),name='CartFoodList'),
    
    
    
    path("orders/create",OrderCreate.as_view(),name='OrderCreate'),
    path("orders/",OrderListALl.as_view(),name='OrderListAll'),
    path("orders/<int:pk>",OrderDetail.as_view(),name='cartDetail'),
    path("orders/cancel",OrderCancelList.as_view(),name='OrderCancelList'),
    path("orders/complete",OrderCompleteList.as_view(),name='OrderCompleteList'),
    path("orders/proccess",OrderProccessingList.as_view(),name='OrderProccessList'),
    path("orders/<int:pk>/status",OrderChangeStatus.as_view(),name='OrderChangeStatus'),
    path("orders/<int:pk>/restaurantUpdate",OrderSetRestaurant.as_view(),name='OrderSetRestaurant'),

    
    
    path("address/create",AddressCreate.as_view(),name='AddressCreate'),
    path("address",AddressListAll.as_view(),name='AddressListAll'),
    path("address/<int:pk>",AddressDetail.as_view(),name='AddressDetail'),


    path("discount/",DiscountCreate.as_view(),name='DiscountCreate'),
    path("discount/<int:pk>",DiscountDetail.as_view(),name='DiscountDetail'),
    path("discount/<str:code>",DiscountCode.as_view(),name='DiscountGetCode'),



    

    

    


    
    

    
    
      
]
