from django.db import models


class Categorias(models.Model):
    categoria_nombre = models.CharField(max_length=100)
    categoria_descripcion = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        ordering = ('-id',)


class Proveedores(models.Model):
    proveedor_nombre = models.CharField(max_length=50)
    proveedor_apellido = models.CharField(max_length=50)
    proveedor_razon_social = models.CharField(max_length=100)
    proveedor_direccion = models.CharField(max_length=50)
    proveedor_tefefono = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id',)

class Productos(models.Model):
    producto_nombre = models.CharField(max_length=100)
    producto_descripcion = models.CharField(max_length=64, null=True, blank=True)
    producto_costo = models.IntegerField()
    producto_precio_venta = models.IntegerField()
    producto_stock = models.IntegerField()
    producto_stock_minimo = models.IntegerField()
    producto_categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='Categoria')
    producto_proveedor = models.ForeignKey(Proveedores, on_delete=models.PROTECT, related_name='Proveedor')
    
    class Meta:
        ordering = ('-id',)