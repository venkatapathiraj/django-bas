from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db import connection


# Create your models here.
class Catogery(models.Model):

    title = models.CharField(max_length=100)
    
    def __str__(self):

        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField()
    weight = models.CharField(max_length=20)
    price = models.FloatField()
    delv = models.CharField(max_length=100)


    def __str__(self):

        return self.name

class Cart(models.Model):
    
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateField(auto_now_add=True)
    def __str__(self):

        return f'{self.quantity} of {self.item.name}'


class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.user.username



