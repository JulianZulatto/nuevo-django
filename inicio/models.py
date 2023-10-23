from django.db import models

# Create your models here.
class Paleta(models.Model):
    marca = models.CharField(max_length=30)#suele tener limite de caracteres 
    descripcion = models.TextField()#no tiene limite de caracteres
    anio = models.IntegerField()