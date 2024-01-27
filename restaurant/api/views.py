import re
from typing import List
from rest_framework import permissions
from rest_framework.generics import *
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render ,get_object_or_404
from .models import *
from .serializers import *
# from django.views.generic import *

# Create your views here.



# class AddressList(ListAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
    


class RestaurantListAll(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    
class RestaurantNearest(ListAPIView):
    queryset = Restaurant.objects.all().order_by('distance_to_origin')
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    

class RestaurantFreeDelivery(ListAPIView):
    queryset = Restaurant.objects.filter(delivery_cost=0)
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    
    
class RestaurantPopularList(ListAPIView):
    queryset = Restaurant.objects.all().order_by('-rate')
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    

    
class FoodListAll(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    
    
class FoodNameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "name"
    permission_classes = [permissions.AllowAny]
    


class FoodPKDetail(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    
    
class FoodPopularList(ListAPIView):
    queryset = Food.objects.all().order_by('-rate')
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    


class FoodfastFoodList(ListAPIView):
    queryset = Food.objects.filter(category='Fa')
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    


class FoodTraditionalFoodList(ListAPIView):
    queryset = Food.objects.filter(category='TR')
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    

class FoodForeignFoodList(ListAPIView):
    queryset = Food.objects.filter(category='FO')
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    
    
    
class MyUserListAll(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class MyUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    
    


class MyUserFoodLikeDetail(ListAPIView):
    # queryset = MyUser_foodLike.objects.all()
    # serializer_class = MyUserFavoriteFoodSerializer
    serializer_class = FoodSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        
        food = MyUser_foodLike.objects.filter(user=user_id).values_list('food_id', flat=True)
        # print(list(food))
        return Food.objects.filter(id__in = food)
        
        
        # return MyUser_foodLike.objects.filter(user=user_id)
    

class MyUserRestaurantLikeDetail(ListAPIView):
    # queryset = MyUser.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        # user = self.request.user
        # self.check_object_permissions(self.request, obj)
        restaurant =  MyUser_restaurantLike.objects.filter(user=user_id).values_list('restaurant_id', flat=True)
        return Restaurant.objects.filter(id__in = restaurant)
        # return MyUser_restaurantLike.objects.filter(user=user_id)
    
class MyUserRestaurantLikeAdd(CreateAPIView):
    queryset = MyUser_restaurantLike.objects.all()
    serializer_class = MyUserFavoriteRestaurantSerializer
    
    # def perform_create(self, serializer):
    #     # Assign the current user to the "user" field before saving
    #     serializer.save(user=self.request.user)
    

class MyUserFoodLikeAdd(CreateAPIView):
    queryset = MyUser_foodLike.objects.all()
    serializer_class = MyUserFavoriteFoodSerializer
    
    
class CartListAll(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    
    def perform_update(self, serializer):
        
        
        super().perform_update(serializer)


        instance = serializer.instance
        
        
        # cart_id = instance.id
        # cart_food = Cart_food(Cart_food.objects.filter(cart = cart_id).first)
        # food_id = cart_food.food
        # food = Food(Food.objects.get(id = food_id))
        # restaurant_id = food.restaurant
        # instance.restaurant = restaurant_id
        
        
        # restaurant = Restaurant(Restaurant.objects.get(id=restaurant_id))
        
        
        
        # restaurant = None
        total_amount = 0
        for cart_food in Cart_food.objects.filter(cart=instance):
            total_amount += int(cart_food.food.price) * int(cart_food.number_food)
            # isinstance.restaurant = cart_food.food.restaurant


        # cart_id = instance.id
        
        # cart_food = Cart_food(Cart_food.objects.filter(cart = cart_id).first)
        
        # food_id = cart_food.food
        # food = Food(Food.objects.filter(id = food_id).first)
        # restaurant_id = food.restaurant
        # instance.restaurant = restaurant_id
        
        # restaurant = Restaurant(Restaurant.objects.get(id = restaurant_id))
        
        instance.total_amount = total_amount
        instance.save()
        
        
        return Response(self.get_serializer(instance).data)
    
class OrderListALl(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
  
 
    
class CartAddFood(CreateAPIView):
    queryset = MyUser_foodLike.objects.all()
    serializer_class = CardAddFoodSerializer


class CartFoodList(ListAPIView):
    # queryset = Cart_food.objects.filter(cart='pk')
    serializer_class = CardAddFoodSerializer
    
    def get_queryset(self):
        cart_id = self.kwargs['pk']
        return Cart_food.objects.filter(cart=cart_id)
    

class CartCreate(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddressCreate(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressListAll(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressUserList(ListAPIView):
    serializer_class = User_addressSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return userAddress.objects.filter(user=user_id)
    

class UserAddressAdd(CreateAPIView):
    queryset = userAddress.objects.all()
    serializer_class = User_addressSerializer
    
    
class UserUpdateProfile(UpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserUpdateSerializer
    

class OrderCancelList(ListAPIView):
    queryset = Order.objects.filter(status='ca')
    serializer_class = OrderSerializer


class OrderCompleteList(ListAPIView):
    queryset = Order.objects.filter(status='co')
    serializer_class = OrderSerializer

class OrderProccessingList(ListAPIView):
    queryset = Order.objects.filter(status='pr')
    serializer_class = OrderSerializer
    
    
class OrderChangeStatus(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderChangeStatusSerializer

    

class OrderSetRestaurant(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    def perform_update(self, serializer):
        
        
        super().perform_update(serializer)


        instance = serializer.instance
        
        
        cart_id = instance.cart
        cart_food = Cart_food(Cart_food.objects.get(cart = cart_id))
        food_id = cart_food.food
        food = Food(Food.objects.get(id = food_id))
        restaurant_id = food.restaurant
        instance.restaurant = restaurant_id

        # instance.total_amount = total_amount
        instance.save()
        
        
        return Response(self.get_serializer(instance).data)


class DiscountCreate(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountDetail(RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
 
 
class DiscountCode(ListAPIView):
    serializer_class = DiscountSerializer

    def get_queryset(self):
        code = self.kwargs['code']
        return Discount.objects.filter(code_discount=code)

