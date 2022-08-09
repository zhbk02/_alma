from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=120)


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    
