from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
