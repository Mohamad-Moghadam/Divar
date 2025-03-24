from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from product.models import Product

class User(models.Model):
    name = models.CharField(max_length = 100)
    number = PhoneNumberField(unique = True, region = "IR")
    national_id_number = models.IntegerField()
    products = models.ForeignKey(to = Product, on_delete = models.PROTECT, related_name = "products_of_each_user")