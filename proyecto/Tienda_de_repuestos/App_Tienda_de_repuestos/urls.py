from django.urls import path
from .views import products, my_orders, my_profile, contact, login_user, logout_user, sign_up, shop_cart, add_product, sub_product, clear_cart, delete_product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'App_Tienda_de_repuestos'

urlpatterns = [
    path('products/', products, name='products'),
    path('orders/', my_orders),
    path('profile/', my_profile),
    path('contact/', contact),
    path('signup/', sign_up, name='SignUp'),
    path('login/', login_user, name='LogIn'),
    path('logout/', logout_user, name='LogOut'),
    path('my_cart/', shop_cart, name='Cart'),
    path('add_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', add_product, name='AddProduct'),
    path('substract_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', sub_product, name='SubProduct'),
    path('delete_product/(?P<product_id>[a-zA-Z0-9_-]+)/$', delete_product, name='DeleteProduct'),
    path('clear_cart/', clear_cart, name='ClearCart'),
        ]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)