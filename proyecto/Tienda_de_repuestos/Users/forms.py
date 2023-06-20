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

class EditProfile(forms.Form):
    first_name = forms.CharField(label="Nombre")      
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Teléfono")
    address = forms.CharField(label="Dirección", max_length=(20))
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'email')