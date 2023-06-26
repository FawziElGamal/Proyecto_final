from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from .models import Client
from .signals import delete_old_avatar_file
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save()

            id_user = User.objects.get(username=form.cleaned_data['username']).pk

            clients = Client(dni=form.cleaned_data['dni'], 
                            phone=form.cleaned_data['phone'], 
                            address=form.cleaned_data['address'],
                            user_id=id_user,
                            avatar= 'Users/avatars/noneavatar.png')
                            
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

@login_required
def my_profile(request):

    user = request.user
    info_user, _ = Client.objects.get_or_create(user_id=user.id)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            if data["first_name"]:
                user.first_name = data["first_name"]
            if data["last_name"]:
                user.last_name = data["last_name"]
            if data["email"]:
                user.email = data["email"]
            if data['phone']:
                info_user.phone = data['phone']
            if data['address']:
                info_user.address = data['address']
            if data["avatar"] != None:
                info_user.avatar = data['avatar']
            if data["url"]:
                info_user.url = data['url']
            
            user.save()
            info_user.save()

        return redirect("Users:EditProfile")
    else:
        user_info = Client.objects.raw(f"SELECT * FROM Users_client WHERE user_id = {user.id}")
        user_info_list = list()
        for info in user_info:
            user_info_list.append(info.dni)
            user_info_list.append(info.phone)
            user_info_list.append(info.address)
            user_info_list.append(info.avatar)
            user_info_list.append(info.url)

        form = EditProfileForm(initial={"first_name": user.first_name, "last_name": user.last_name, "email": user.email, "phone": user_info_list[1], "address": user_info_list[2]})
        return render(request, "Users/edit_profile.html", {"form": form, "user_info": user_info_list})