from django.db import models
from app_categorias.models import Categorias


class Productos(models.Model):
    producto_nombre = models.CharField(max_length=100)
    producto_descripcion = models.CharField(max_length=64, null=True, blank=True)
    producto_costo = models.IntegerField()
    producto_precio_venta = models.IntegerField()
    producto_stock = models.IntegerField()
    producto_stock_minimo = models.IntegerField()
    producto_category = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='Categoria')

    
    class Meta:
        ordering = ('-id',)