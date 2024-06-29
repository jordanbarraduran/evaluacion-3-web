from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    categoria   = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    imagen      = models.ImageField(upload_to='productos/', default='media/default.webp')

    def __str__(self):
        return self.nombre