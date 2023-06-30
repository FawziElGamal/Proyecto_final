from django.urls import path
from .views import products, all_orders, individual, my_orders, shop_cart, add_product, sub_product, clear_cart, delete_product, confirm_order

app_name = 'App_Tienda_de_repuestos'

urlpatterns = [
    path('products/', products, name='products'),
    path('all_orders/', all_orders, name='AllOrders'),
    path('my_orders/', my_orders, name='MyOrders'),
    path('my_cart/', shop_cart, name='Cart'),
    path('add_product/<str:product_id>/', add_product, name='AddProduct'),
    path('substract_product/<str:product_id>/', sub_product, name='SubProduct'),
    path('delete_product/<str:product_id>/', delete_product, name='DeleteProduct'),
    path('clear_cart/', clear_cart, name='ClearCart'),
    path('confirm_order/', confirm_order, name='ConfirmOrder'),
    path('confirm_order/', confirm_order, name='ConfirmOrder'),
    path('products/(?P<product_id>[a-zA-Z0-9_-]+)/$', individual, name='IndividualProduct'),
        ]