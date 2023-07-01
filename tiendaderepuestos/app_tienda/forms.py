from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    dni = forms.IntegerField(label="DNI")
    phone = forms.IntegerField(label="Teléfono")
    address = forms.CharField(label="Dirección", max_length=(20))
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'password1', 'password2')