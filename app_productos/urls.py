from django.urls import include
from django.conf.urls import url

from rest_framework import routers

from .views import CategoriassViewSet, ProductosViewSet

router_productos = routers.DefaultRouter()
router_productos.register(r'categorias', CategoriassViewSet, basename='categorias'),
router_productos.register(r'productos', ProductosViewSet, basename='productos'),
router_productos.register(r'proveedores', ProductosViewSet, basename='proveedores'),

urlpatterns = [
    url('/', include(router_productos.urls)),
]