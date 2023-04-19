from django.contrib import admin

# Register your models here.
from .models import Categorias


@admin.register(Categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_nombre', 'categoria_descripcion')
    search_fields = ['id', ]