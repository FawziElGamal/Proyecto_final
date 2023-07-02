from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    dni = forms.IntegerField(label="DNI")
    phone = forms.IntegerField(label="Teléfono")
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Dirección", max_length=(20))
    username = forms.CharField(label="Nombre de usuario (nick)", help_text="Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text="Su contraseña no puede ser muy similar a su otra información personal.\nSu contraseña debe contener al menos 8 caracteres.\n \nSu contraseña no puede ser una contraseña de uso común.\nSu contraseña no puede ser completamente numérica.")
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'dni', 'phone', 'address', 'email', 'username', 'password1', 'password2')

class EditProfileForm(forms.Form):
    first_name = forms.CharField(label="Nombre", required=False)      
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Email", required=False)
    phone = forms.IntegerField(label="Teléfono", required=False)
    address = forms.CharField(label="Dirección", max_length=(20), required=False)
    avatar = forms.ImageField(required=False)
    url = forms.URLField(label="Redes/URL" ,required=False)
    # class Meta:
    #     model = Client
    #     fields = ('first_name', 'last_name', 'email')

class ChangePass(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput, help_text="Ingrese su contreña actual.")
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, help_text="Su contraseña no puede ser muy similar a su otra información personal.\nSu contraseña debe contener al menos 8 caracteres.\n \nSu contraseña no puede ser una contraseña de uso común.\nSu contraseña no puede ser completamente numérica.")
    new_password2 = forms.CharField(label="Confirmar nueva contraseña", widget=forms.PasswordInput, help_text="Reescriba la constraseña ingresada")
    class Meta:
        model=User
        fields=('old_password', 'new_password1', 'new_password2')






