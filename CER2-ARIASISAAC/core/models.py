from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    info = models.CharField(max_length=128)
    precio = models.IntegerField()
    imagen = models. ImageField(null=True, blank=True, upload_to="productos");
    def __str__(self):
        return f'{self.nombre}->{self.precio}'







class Pedido(models.Model):
    
    nombre = models.CharField(max_length=64)
    cantidad = models.IntegerField()
    precio_parcial = models.IntegerField()
    estado = models.CharField(max_length=10)
    correo = models.EmailField(max_length=128)    

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades"