from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Productos, Categorias, Proveedores


class ProductosSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class CategoriasSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProveedoresSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'