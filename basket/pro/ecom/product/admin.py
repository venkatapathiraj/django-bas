from django.contrib import admin
from .models import Catogery,Product,Cart,Order

# Register your models here.

admin.site.register(Catogery)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)