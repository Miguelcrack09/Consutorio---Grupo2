from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.deletion import CASCADE
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(max_length=2, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre
        

class Citas(models.Model):
      fecha = models.DateField()
      hora = models.DateTimeField()
      paciente = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
      cormobilidad = models
      sintomas = models.CharField(max_length=45, blank=True, null=True)
      horassintomas = models.IntegerField(max_length=2, blank=True, null=True)

      def __str__(self):
          return '{} {} {}'.format(self.paciente, self.fecha, self.hora)
    
    

# class Resultado(models.Model):
#     medico = 
#     paciente = 
#     diagnostico = 
#     fecha = models.ForeignKey(Citas, verbose_name=_("fecha"), on_delete=models.CASCADE)
#     hora = models.ForeignKey(Citas, verbose_name=_("hora"), on_delete=models.CASCADE)
#     models.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
