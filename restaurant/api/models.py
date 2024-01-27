from tkinter import N
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from ast import Delete
from re import A, S, T
from django.contrib.auth.models import AbstractUser
import email
from pyexpat import model
from sre_parse import CATEGORIES
from unicodedata import category, name
from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.city + self.state + self.street + self.zipCode




    
    
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,unique=True)
    rate = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    isOpen = models.BooleanField(default=True)
    restaurant_type = models.CharField(max_length=60)
    restaurant_discription = models.TextField(max_length=200,null=True)
    delivery_cost = models.IntegerField(default=0)
    distance_to_origin = models.IntegerField()
    # foods = models.ManyToManyField(Food,blank=True,related_name='restaurants')
    restaurant_image = models.ImageField()
    
    
    def __str__(self):
        return self.name

CATEGORIES = [
    ('Fa','fastfood'),
    ('Tr','traditional'),
    ('Fo','foreignfood')
]
class Food(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=2,choices=CATEGORIES)
    description = models.TextField()
    price = models.IntegerField(default=0)
    rate = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    food_image = models.ImageField()
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class MyUser(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # email = models.EmailField(unique=True, blank=False, null=False,required=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50)
    birthDate = models.DateTimeField(null=True)
    address = models.ManyToManyField(Address)
    profile_image = models.ImageField()
    foods_like = models.ManyToManyField(Food,blank=True)
    restaurant_like = models.ManyToManyField(Restaurant,blank=True)


    # def __init__(self, *args, **kwargs):
    #     super(MyUser, self).__init__(*args, **kwargs)
    #     # Set the default value of is_active to False when creating a new user
    #     self.is_active = False
        
    def __str__(self):
        return self.first_name + self.last_name



    
    
class Cart(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    # foods = models.ManyToManyField(Food,blank=True)
    

ORDER_STATUS = [
    ('pr','Processing'),
    ('ca','Cancel'),
    ('co','Complete')
]
class Order(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address_delivery = models.ForeignKey(Address,on_delete=models.CASCADE)
    timeCreated = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    status = models.CharField(choices=ORDER_STATUS,max_length=2,default='pr')


class Address_Order(models.Model):
    address = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Food,on_delete=models.CASCADE,null=True)
    

#     def __str__(self):
#         return self.restaurant + self.food
    
    
class Cart_food(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE,null=True)
    number_food = models.PositiveIntegerField(default=1)
    
    
    def clean(self):
        # Ensure the Cart and Food belong to the same Restaurant
        if self.cart.restaurant != self.food.restaurant:
            raise ValidationError("Cannot add food to cart from a different restaurant.")

    # def save(self, *args, **kwargs):
    #         # If the cart is not set, create a new Cart and set its restaurant based on the food
    #     if not self.cart_id:
    #         cart = Cart.objects.create(restaurant=self.food.restaurant)
    #         self.cart = cart

        
        super(Cart_food, self).save(*args, **kwargs)
        
        self.cart.save()
        # def __str__(self):
    #     return self.cart + self.food
    
    
    
class userAddress(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

    
    # def __str__(self):
    #     return self.address + self.user
    
    
class MyUser_foodLike(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE,null=True)

    # def __str__(self):
    #     return self.user + self.food


class MyUser_restaurantLike(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)

    # def __str__(self):
    #     return self.cart + self.food



class Discount(models.Model):
    percent_discount = models.IntegerField(default=0)
    code_discount = models.CharField(max_length=10,null=True,blank=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code_discount    
        


class Cart_Restaurant(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)

    
     

    
    
    
