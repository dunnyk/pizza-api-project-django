from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_status', 'size', 'quantity', 'create_at']
    list_filter = ['order_status', 'create_at', 'size']
