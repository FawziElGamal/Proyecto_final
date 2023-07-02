from django.urls import path
from .views import products, all_orders, individual, my_orders, shop_cart, add_product, sub_product, clear_cart, delete_product, confirm_order

app_name = 'app_tienda'

urlpatterns = [
    path('products/', products, name='Products'),
    path('index/', products, name='Products'),
    path('all-orders/', all_orders, name='AllOrders'),
    path('my-orders/', my_orders, name='MyOrders'),
    path('my-cart/', shop_cart, name='Cart'),
    path('add-product/<str:product_id>/', add_product, name='AddProduct'),
    path('substract-product/<str:product_id>/', sub_product, name='SubProduct'),
    path('delete-product/<str:product_id>/', delete_product, name='DeleteProduct'),
    path('clear-cart/', clear_cart, name='ClearCart'),
    path('confirm-order/', confirm_order, name='ConfirmOrder'),
    path('products/<str:product_id>/', individual, name='IndividualProduct'),
        ]