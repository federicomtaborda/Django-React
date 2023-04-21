from django.contrib import admin

# Register your models here.
from .models import Productos, Categorias, Proveedores


@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_nombre', 'producto_descripcion',
    'producto_costo', 'producto_precio_venta',
    'producto_stock', 'producto_stock_minimo',
    'producto_categoria',)
    search_fields = ['id', ]


@admin.register(Categorias)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', ]


@admin.register(Proveedores)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', ]