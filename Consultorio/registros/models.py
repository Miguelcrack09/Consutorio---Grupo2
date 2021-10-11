from django.db import models
#from django.core.urlresolvers import reverse_lazy

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    cedula = models.IntegerField()
    edad = models.IntegerField()
    genero = models.CharField(max_length=45, blank=True, null=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre
        

# class Resultado(models.Model):
#     medico = 
#     paciente = 
#     diagnostico = 
#     fecha = models.ForeignKey(Citas, verbose_name=_("fecha"), on_delete=models.CASCADE)
#     hora = models.ForeignKey(Citas, verbose_name=_("hora"), on_delete=models.CASCADE)
#     models.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
