from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'user',
        'dni',
        'phone'
    ]
    search_fields = ('user', 'dni', 'phone')
    ordering = ('user', 'dni')
    list_editable = ('phone',)