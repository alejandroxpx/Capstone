from audioop import maxpp
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

class Pet(models.Model):
    name = models.CharField(max_length=64)
    breed = models.CharField(max_length=64)
    age = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    image = models.ImageField(upload_to="static/")
    location = models.CharField(max_length=64)
