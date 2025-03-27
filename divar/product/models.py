from django.db import models
from user.models import User

class Product(models.Model):
    name = models.CharField(max_length = 100)
    location = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")