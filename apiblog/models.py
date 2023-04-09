from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField('Categoria', max_length=70, blank=False, null=False)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return u'{0}'.format(self.category)

class Blog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuario",
        blank=True, null=True
    )
    description = models.CharField('Descripción', max_length=70, unique=True)
    category = models.ForeignKey(
        Category,
        related_name='Categoria',
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Categoria"
    )