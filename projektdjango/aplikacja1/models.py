from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)