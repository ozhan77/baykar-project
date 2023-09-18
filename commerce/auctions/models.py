from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Logs(models.Model):
    transaction = models.CharField(max_length=200)
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category" )
    def __str__(self):
        return self.brand