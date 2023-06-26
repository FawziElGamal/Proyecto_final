from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'full_name',
        'email',
        'phone',
        'msg'
    ]
    search_fields = ('id', 'full_name', 'email', 'phone', 'msg')
    ordering = ('id', 'full_name', 'email')