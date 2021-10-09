from django.db import models
from django.contrib import admin
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(max_length=2, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=45, blank=True, null=True)
    rol = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.correo
    
    def __str__(self) -> str:
        return self.nombre

admin.site.register(Usuario)