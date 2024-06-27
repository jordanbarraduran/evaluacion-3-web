from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)
    

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='media/default.webp')

    def __str__(self):
        return self.nombre