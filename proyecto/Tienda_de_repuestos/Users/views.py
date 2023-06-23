from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, EditProfile
from django.contrib.auth.models import User
from .models import Client
from django.db import connection

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
        
    user = request.user

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.save()

            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE Users_client SET phone = {data['phone']}, address = '{data['address']}' WHERE user_id = {user.id}")

            if data["avatar"] != None:
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE Users_client SET avatar = {data['avatar']} WHERE user_id = {user.id}")

        return HttpResponse("Gracia")
    else:
        user_info = Client.objects.raw(f"SELECT * FROM Users_client WHERE user_id = {user.id}")
        user_info_list = list()
        for info in user_info:
            user_info_list.append(info.dni)
            user_info_list.append(info.phone)
            user_info_list.append(info.address)
            user_info_list.append(info.avatar)

        form = EditProfile(initial={"first_name": user.first_name, "last_name": user.last_name, "email": user.email, "phone": user_info_list[1], "address": user_info_list[2]})
        return render(request, "Users/edit_profile.html", {"form": form, "user_info": user_info_list})