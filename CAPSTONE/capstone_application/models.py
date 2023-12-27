from audioop import maxpp
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    # location = models.CharField(max_length=64)

    def __str__ (self):
        return f"id: {self.id}: username: {self.username} password: {self.password} name: {self.name}"


