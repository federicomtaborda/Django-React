from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductosSerialezer, CategoriasSerialezer, ProveedoresSerialezer
from .models import Productos, Categorias, Proveedores


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerialezer


class CategoriassViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerialezer


class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerialezer
