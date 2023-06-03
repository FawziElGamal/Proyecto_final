from django.contrib import admin
from .models import Client, Product, Order

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
        'client_dni',
        'product_id',
        'quantity',
        'total_usd_price'
    ]
    # search_fields = ('client_dni', 'product_id', 'quantity')
    ordering = ('client_dni', 'product_id', 'quantity', 'total_usd_price')
    list_editable = ('quantity',)