from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    msg = models.TextField()