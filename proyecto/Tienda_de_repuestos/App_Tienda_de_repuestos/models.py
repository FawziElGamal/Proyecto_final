from django.db import models

# Create your models here.

class Clientes(models.Model):

    dni = models.IntegerField()
    nombre = models.CharField(max_length=20)