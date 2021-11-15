from django.contrib import admin
from .models import Voucher, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Voucher)
