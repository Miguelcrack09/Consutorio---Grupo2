from django.db import models

# Create your models here.
class Citas(models.Model):
    fecha = models.DateField()
    hora = models.DateTimeField()
    paciente = models.CharField(max_length=45, blank=True, null=True)
    cormobilidad = models.CharField(max_length=45, blank=True, null=True)
    sintomas = models.CharField(max_length=45, blank=True, null=True)
    horassintomas = models.IntegerField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.paciente