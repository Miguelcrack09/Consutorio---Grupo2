from django.db import models

# Create your models here.
class Citas(models.Model):
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    paciente = models.CharField(max_length=45, blank=True, null=True)
    cormobilidad = models.CharField(max_length=45, blank=True, null=True)
    sintomas = models.CharField(max_length=45, blank=True, null=True)
    horassintomas = models.IntegerField()

    def __str__(self) -> str:
        return self.paciente