from distutils.command.upload import upload
from django.db import models
import base64 
from django.core.files.base import ContentFile


# Create your models here.
class libro(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    añoedicion = models.CharField(max_length=20)
    preciocompra = models.DecimalField(max_digits = 10, decimal_places = 2)
    precioalquiler = models.DecimalField(max_digits = 10, decimal_places = 2)
    disponible = models.BooleanField()
    portada = models.ImageField(upload_to="portadas", null=True)
    created_at = models.DateTimeField(auto_now_add='true')

class persona(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='nombre')
    apellido = models.CharField(max_length=25, verbose_name='apellido')
    cedula = models.CharField(max_length=20, verbose_name='cedula')
    direcion = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    
class facturacion(models.Model):
    fecha = models.DateTimeField(auto_now_add="true")
    usuario = models.ForeignKey('usuario',null=True, on_delete=models.SET_NULL)
    libro = models.ForeignKey('libro', null=True, on_delete=models.SET_NULL)
    valor = models.FloatField()

class usuario(models.Model):
    contraseña = models.CharField(max_length=12)
    usuario = models.CharField(max_length=40)
    persona = models.ForeignKey('persona', null=True, on_delete=models.SET_NULL)