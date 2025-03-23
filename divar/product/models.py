from django.db import models

class Product:
    name = models.CharField(max_length = 100)
    