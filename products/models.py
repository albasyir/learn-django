from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=2083)
    stock = models.IntegerField(default=0)


class Voucher(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=254)
    discount = models.FloatField()
