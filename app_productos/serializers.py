from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Productos, Categorias, Proveedores


class ProveedoresSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['id', 'proveedor_nombre',
        'proveedor_apellido', 'proveedor_razon_social']


class CategoriasSerialezer(serializers.ModelSerializer):
    
    class Meta:
        model = Categorias
        fields = '__all__'


class ProductosSerialezer(serializers.ModelSerializer):
    producto_proveedor = ProveedoresSerialezer(many=False, read_only=True)
    producto_categoria = CategoriasSerialezer(many=False, read_only=True)

    class Meta:
        model = Productos()
        fields = '__all__'

