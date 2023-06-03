from django.urls import path
from .views import home, products, my_orders, my_profile, contact


urlpatterns = [
    path('', home),
    path('products/', products),
    path('orders/', my_orders),
    path('profile/', my_profile),
    path('contact/', contact),
        ]