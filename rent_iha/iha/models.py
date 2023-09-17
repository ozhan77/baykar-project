from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.category_name
class iha (models.Model):
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    weight=models.CharField(max_length=10)
    image =models.ImageField(upload_to='item_images', blank=True, null=True)
    condition=models.CharField(max_length=20)
    isrented=models.BooleanField(default=False)
    category = models.ForeignKey (Category, related_name='items', on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.model

