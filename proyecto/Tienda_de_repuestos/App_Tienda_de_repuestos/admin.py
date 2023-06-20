from django.contrib import admin
from .models import Client, Product, Order, OrderProducts

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'user',
        'dni',
        'phone'
    ]
    # search_fields = ('user', 'dni', 'phone')
    ordering = ('user', 'dni')
    list_editable = ('phone',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= [
        'part_number',
        'quantity',
        'location',
        'description',
        'price_usd'
    ]
    # search_fields = ('part_number', 'location', 'description', 'price_usd')
    ordering = ('part_number', 'location', 'description', 'price_usd')
    list_editable = ('quantity', 'location', 'price_usd')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'order_date',
        'client_dni',
        'paid'
    ]
    # search_fields = ('client_dni', 'product_id', 'quantity')
    ordering = ('order_date', 'client_dni')
    list_editable = ('paid',)

@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display= [
        'order_id_id',
        'part_number_id',
        'quantity'
    ]
    # search_fields = ('client_dni', 'product_id', 'quantity')
    ordering = ('order_id_id',)
    list_editable = ('quantity',)