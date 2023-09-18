from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


    #tarih
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    weight=models.FloatField(max_length=10)
    imageUrl = models.CharField(max_length=100)
    price = models.FloatField(default=True)
    isActive = models.BooleanField(default=True)
    rented = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category" )
    
    def __str__(self):
        return self.brand

class Logs(models.Model):
    transaction = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)

class Rentlist(models.Model):
    customer=models.CharField(max_length=200)
    iha=models.CharField(max_length=200)
    rentStartDate = models.DateTimeField(blank=True, null=True)
    rentFinishDate= models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)