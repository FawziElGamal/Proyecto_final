from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    dni = forms.IntegerField(label="DNI")
    phone = forms.IntegerField(label="Teléfono")
    address = forms.CharField(label="Dirección", max_length=(20))
    avatar = forms.ImageField()
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class EditProfile(forms.Form):
    first_name = forms.CharField(label="Nombre", required=False)      
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Email", required=False)
    phone = forms.IntegerField(label="Teléfono", required=False)
    address = forms.CharField(label="Dirección", max_length=(20), required=False)
    avatar = forms.ImageField(required=False)
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'email')