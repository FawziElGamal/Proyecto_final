from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, "App_Tienda_de_repuestos/index.html")

def products(request):
    return HttpResponse("Productos")

def my_orders(request):
    return HttpResponse("Mis pedidos")

def my_profile(request):
    return HttpResponse("Mi perfil")

def contact(request):
    return HttpResponse("Contacto")




def probando_template_2(request):
    
    ahora = datetime.now()
        

    # clientes = Clientes.objects.all()


    # context = {"clientes": clientes,
    #            "hora": ahora}

    # return render(request, "App_Tienda_de_repuestos/index.html", context=context)