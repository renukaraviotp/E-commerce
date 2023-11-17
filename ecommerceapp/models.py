from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    productname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/') 

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/') 
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    