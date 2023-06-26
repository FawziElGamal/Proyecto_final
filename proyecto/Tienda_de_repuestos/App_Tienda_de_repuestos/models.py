from django.db import models
from Users.models import Client


# Create your models here.
class Product(models.Model):
    part_number = models.CharField(max_length=20, primary_key=True)
    quantity = models.IntegerField(null=False)
    location = models.CharField(max_length=5)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='App_Tienda_de_repuestos/products')
    price_usd = models.FloatField(null=False)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    client_dni = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    paid = models.BooleanField(default=False)


class OrderProducts(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    part_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()