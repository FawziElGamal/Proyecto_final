from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Client, Order, OrderProducts
from django.db.models import Q
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

    unpaid_orders = Order.objects.raw("SELECT id FROM App_Tienda_de_repuestos_order WHERE paid = 0")

    unpaid_orders_list = []
    for order in unpaid_orders:
        unpaid_orders_details = OrderProducts.objects.raw(f"SELECT id, part_number_id, quantity FROM App_Tienda_de_repuestos_orderproducts WHERE order_id_id = {order.id}")
        descriptions = []
        for part_number in unpaid_orders_details:
            description = Product.objects.get(part_number=part_number.part_number_id)
            descriptions.append(description)
        unpaid_orders_list.append({
            'order': order,
            'products': unpaid_orders_details,
            'descriptions': descriptions
        })

    paid_orders = Order.objects.filter(paid=True)
    paid_orders_list = []
    for order in paid_orders:
        paid_orders_details = OrderProducts.objects.filter(order_id=order.id)
        paid_orders_list.append({
            'order': order,
            'products': paid_orders_details,
        })

    return render(request, "App_Tienda_de_repuestos/orders.html", {'unpaid_orders_list': unpaid_orders_list, 'paid_orders_list': paid_orders_list})

def my_profile(request):
    return HttpResponse("Mi perfil")

def contact(request):
    return HttpResponse("Contacto")


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
    user = Client.objects.raw(f"SELECT dni FROM Users_client")
    order_products = request.POST.getlist('part_number')
    quantities = request.POST.getlist('cantidad')

    for result in user:
        client_dni = result.dni

    order = Order.objects.create(client_dni_id=client_dni)

    for i, part_number in enumerate(order_products):
        product_price = Product.objects.raw(f"SELECT part_number, price_usd FROM App_Tienda_de_repuestos_product WHERE part_number = '{part_number}'")
        for result in product_price:
            quantity = quantities[i]
            OrderProducts.objects.create(order_id_id=order.id, part_number_id=part_number, unit_price=result.price_usd, quantity=quantity)

        

    return HttpResponse("Pedido confirmado")







