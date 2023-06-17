from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Client, Order, OrderProducts
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from .cart import Cart
from django.contrib.auth.decorators import login_required
from django.db import models

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

    return redirect("App_Tienda_de_repuestos:Cart")

def sub_product(request, product_id):
    cart = Cart(request)

    product = Product.objects.get(part_number=product_id)

    cart.subtract_product(product)

    return redirect("App_Tienda_de_repuestos:Cart")

def delete_product(request, product_id):
    cart = Cart(request)

    product = Product.objects.get(id=product_id)

    cart.erase_product(product)

    return redirect("App_Tienda_de_repuestos:products")

def clear_cart(request, product_id):
    cart = Cart(request)

    cart.clear_chart()

    return redirect("App_Tienda_de_repuestos:products")

@login_required
def shop_cart(request):
    cart = Cart(request)

    total_price = []

    for _, cart_items in cart.session.items():
        if isinstance(cart_items, dict):
            for _, value in cart_items.items():
                unit_price = value.get('price')
                quantity_selected = value.get('quantity')
                total_prices = unit_price * quantity_selected
                total_price.append(total_prices)
        
    total_price = (sum(total_price))
    
    return render(request, "App_Tienda_de_repuestos/cart.html", {"total_price": total_price})

def confirm_order(request):

    user = request.user
    user = Client.objects.raw(f"SELECT dni FROM App_Tienda_de_repuestos_client")
    order_products = request.POST.getlist('part_number')
    quantities = request.POST.getlist('cantidad')

    for result in user:
        client_dni = result.dni
    # print(part_number)
    # print(quantities)

    order = Order.objects.create(client_dni_id=client_dni)

    for part_number in order_products:
        product_price = Product.objects.raw(f"SELECT part_number, price_usd FROM App_Tienda_de_repuestos_product WHERE part_number = '{part_number}'")
        for result in product_price:
            for quantity in quantities:
                OrderProducts.objects.create(order_id_id=order.id, part_number_id=part_number, unit_price=result.price_usd, quantity=quantity)

        

    return HttpResponse("Pedido confirmado")







