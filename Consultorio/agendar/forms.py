from django import forms
from django.forms import ModelForm
from .models import Citas

class citasForm(ModelForm):
        model = Citas
        fields = [
                'fecha',
                'hora',
                'paciente',
                'patologia',
                'sintomas',
                'duracionsintoma',
                ]
        
        