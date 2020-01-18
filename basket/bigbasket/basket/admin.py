from django.contrib import admin
from .models import Category, Item, Cart, OrderedItem


# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(OrderedItem)