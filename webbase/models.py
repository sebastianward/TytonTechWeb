from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    categoria = models.TextField(null=False, blank=False)
    proveedor = models.CharField(max_length=200, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    img_url = models.URLField(max_length=200, null=False, blank=False)
    estado = models.IntegerField(null=False, blank=False)
    en_stock = models.IntegerField( null=False, blank=False)

    class Meta:
        db_table = 'PRODUCTO'

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.TextField()    

    class Meta:
        db_table = 'CATEGORIA'

class SubCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.TextField()    

    class Meta:
        db_table = 'SUBCATEGORIA'

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField(null=False, blank=False)
    id_producto = models.IntegerField(null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'CARRO'

