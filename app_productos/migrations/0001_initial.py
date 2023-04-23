# Generated by Django 3.2.10 on 2023-04-20 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nombre', models.CharField(max_length=100)),
                ('categoria_descripcion', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor_nombre', models.CharField(max_length=50)),
                ('proveedor_apellido', models.CharField(max_length=50)),
                ('proveedor_razon_social', models.CharField(max_length=100)),
                ('proveedor_direccion', models.CharField(max_length=50)),
                ('proveedor_tefefono', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_nombre', models.CharField(max_length=100)),
                ('producto_descripcion', models.CharField(blank=True, max_length=64, null=True)),
                ('producto_costo', models.IntegerField()),
                ('producto_precio_venta', models.IntegerField()),
                ('producto_stock', models.IntegerField()),
                ('producto_stock_minimo', models.IntegerField()),
                ('producto_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Categoria', to='app_productos.categorias')),
                ('producto_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Proveedor', to='app_productos.proveedores')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
