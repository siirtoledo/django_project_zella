from django.db import models
from datetime import datetime
from shop.models import Category

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="media/products")
    price=models.CharField(max_length=255)
    category=models.ForeignKey(Category,models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title