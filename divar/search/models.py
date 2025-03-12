from django.db import models


class Users(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(null = True, blank = True)
    number = models.CharField(max_length = 13)
    user_location = models.TextField()
