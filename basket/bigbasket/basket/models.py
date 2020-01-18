from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Item(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField()
    weight = models.CharField(max_length=50)
    price = models.FloatField()
    delv = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Cart(models.Model):

    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    pur_date = models.DateField(auto_now_add=False)
    st_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return f'{self.quantity} of {self.item}'


   

           


class OrderedItem(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    orderd = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username


    


