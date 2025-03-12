from django.db import models
from search.models import Users

class Real_State(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    location = models.TextField()
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "seller")


class Vehicle(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "vehicle_seller")
    for_rent = models.BooleanField(default = False)


class Appliance(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "appliance_seller")


class Furniture(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "furniture_seller")


class Service(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    provider = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "service_provider")


class Personal_stuff(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "PS_seller")


class Intertainer(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "intertainer_seller")


class Industrial(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    seller = models.ForeignKey(to = Users, on_delete = models.CASCADE, related_name = "industrial_seller")