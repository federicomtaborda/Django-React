from django.contrib import admin

# Register your models here.
from .models import Productos


@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_nombre', 'producto_descripcion',
    'producto_costo', 'producto_precio_venta',
    'producto_stock', 'producto_stock_minimo',
    'producto_category',)
    search_fields = ['id', ]