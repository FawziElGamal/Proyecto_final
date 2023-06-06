from django.urls import path
from .views import products, my_orders, my_profile, contact

app_name = 'App_Tienda_de_repuestos'

urlpatterns = [
    path('products/', products, name='products'),
    path('orders/', my_orders),
    path('profile/', my_profile),
    path('contact/', contact),
        ]