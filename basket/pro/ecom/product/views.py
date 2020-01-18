from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from product.models import Product, Cart, Order
from django.contrib import messages
# Create your views here.
class Veg(ListView):

    model = Product,Cart

    template_name = "veg1.html"



