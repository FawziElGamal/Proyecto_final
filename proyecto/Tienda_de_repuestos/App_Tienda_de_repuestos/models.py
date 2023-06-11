from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)

class Product(models.Model):
    part_number = models.CharField(max_length=20, primary_key=True)
    quantity = models.IntegerField(null=False)
    location = models.CharField(max_length=5)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='App_Tienda_de_repuestos/products')
    price_usd = models.IntegerField(null=False)

class Order(models.Model):
    client_dni = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    total_usd_price = models.IntegerField()