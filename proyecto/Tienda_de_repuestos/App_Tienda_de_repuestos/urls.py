from django.urls import path
from .views import products, all_orders, my_orders, my_profile, contact, shop_cart, add_product, sub_product, clear_cart, delete_product, confirm_order
from django.conf import settings
from django.conf.urls.static import static

app_name = 'App_Tienda_de_repuestos'

urlpatterns = [
    path('products/', products, name='products'),
    path('all_orders/', all_orders, name='AllOrders'),
    path('my_orders/', my_orders, name='MyOrders'),
    path('profile/', my_profile),
    path('contact/', contact),
    path('my_cart/', shop_cart, name='Cart'),
    path('add_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', add_product, name='AddProduct'),
    path('substract_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', sub_product, name='SubProduct'),
    path('delete_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', delete_product, name='DeleteProduct'),
    path('clear_cart/', clear_cart, name='ClearCart'),
    path('confirm_order/', confirm_order, name='ConfirmOrder'),
        ]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
