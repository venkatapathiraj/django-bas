from django.urls import path,include
from basket.views import Veg,purchases,Rice,Bands,Bever

app_name= 'basket'


urlpatterns = [
    path('',Veg.as_view(), name='veg'),
    path('bev/',Bever.as_view(), name='bev'),
    path('bands/',Bands.as_view(), name='bands'),
    path('rice/',Rice.as_view(), name='rice'),
    path('pur/', purchases,name='pur'),
]
