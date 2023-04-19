from django.db import models


class Categorias(models.Model):
    categoria_nombre = models.CharField(max_length=100)
    categoria_descripcion = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        ordering = ('-id',)