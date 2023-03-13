from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UploadProduct(models.Model):
    class Meta:
        ordering = ["name", "bio"]

    name = models.CharField(max_length=15)
    age = models.IntegerField(default=0)
    bio = models.CharField(max_length=200)


class BuyProduct(models.Model):
    class Meta:
        ordering = []

    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=60)
    comment = models.CharField(max_length=50)