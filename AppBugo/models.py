
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField

class Producto(models.Model):
    nombre = models.CharField
    descripcion = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField
    apellido = models.CharField
