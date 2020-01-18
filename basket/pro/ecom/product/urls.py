from django.urls import path,include
from product.views import Veg


app_name= 'basket'


urlpatterns = [
    path('',Veg.as_view(), name='veg'),
]
