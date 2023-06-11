from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Client
from django.contrib.auth.models import User
from .cart import Cart
from .models import Product

# Create your views here.
def products(request):

    if request.GET.get('search', ''):
        print(request.GET['search'])
        search = request.GET['search']
        fetch = Product.objects.filter(Q(description__icontains=search) | Q(part_number__icontains=search))

    else:    
        fetch = Product.objects.all()

    return render(request, "App_Tienda_de_repuestos/index.html", {'products': fetch})

def my_orders(request):
    return HttpResponse("Mis pedidos")

def my_profile(request):
    return HttpResponse("Mi perfil")

def contact(request):
    return HttpResponse("Contacto")


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
    return render(request, "App_Tienda_de_repuestos/signup.html", {"form": form})


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
    return render(request, "App_Tienda_de_repuestos/login.html", {"form": form})

        
def logout_user(request):
    logout(request)
    return redirect("App_Tienda_de_repuestos:products")


def add_product(request, product_id):
    cart = Cart(request)

    product = Product.objects.get(part_number=product_id)

    cart.add_item(product)

    return redirect("App_Tienda_de_repuestos:products")

def sub_product(request, product_id):
    cart = Cart(request)

    product = Product.objects.get(part_number=product_id)

    cart.subtract_product(product)

    return redirect("App_Tienda_de_repuestos:products")

def delete_product(request, product_id):
    cart = Cart(request)

    product = Product.objects.get(id=product_id)

    cart.erase_product(product)

    return redirect("App_Tienda_de_repuestos:products")

def clear_cart(request, product_id):
    cart = Cart(request)

    cart.clear_chart()

    return redirect("App_Tienda_de_repuestos:products")


def shop_cart(request):
    
    return render(request, "App_Tienda_de_repuestos/cart.html")







