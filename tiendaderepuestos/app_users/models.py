from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    avatar = models.ImageField(upload_to='app_users/avatars')
    url = models.URLField(null=True, blank=True)
    