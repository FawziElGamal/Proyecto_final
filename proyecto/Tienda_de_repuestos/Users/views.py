from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, EditProfile
from django.contrib.auth.models import User
from .models import Client

# Create your views here.
def sign_up(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.save()

            id_user = User.objects.get(username=form.cleaned_data['username']).pk

            clients = Client(dni=form.cleaned_data['dni'], phone=form.cleaned_data['phone'], address=form.cleaned_data['address'], user_id=id_user)
            clients.save()

            login(request, data)
            return redirect("App_Tienda_de_repuestos:products")
        else:
            messages.error(request, "Corrobore los querimientos")
    
    form = SignUpForm()
    return render(request, "Users/signup.html", {"form": form})


def login_user(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect("App_Tienda_de_repuestos:products")
            else:
                messages.error(request, "El usuario y/o contraseña ingresado no es válido")

        else:
            messages.error(request, "El usuario y/o contraseña ingresado no es válido")

    form = AuthenticationForm()
    return render(request, "Users/login.html", {"form": form})

        
def logout_user(request):
    logout(request)
    return redirect("App_Tienda_de_repuestos:products")


def my_profile(request):

    if request.method == "POST":
        user = request.user
    else:
        form = EditProfile()
        return render(request, "Users/edit_profile.html", {"form": form})