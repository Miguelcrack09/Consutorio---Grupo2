from django.forms import ModelForm
from .models import Citas

class citasForm(ModelForm):
        class Meta:
                model = Citas
                fields = [
                        'paciente',
                        'cormobilidad',
                        'sintomas',
                        'horassintomas'
                        ]
        
        
        