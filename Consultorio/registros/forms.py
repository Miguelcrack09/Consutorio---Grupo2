from django.forms import ModelForm
from .models import Usuario 

class UsuarioForm(ModelForm):    
    class Meta:
        model = Usuario
        fields = [
                'nombre',
                'apellido',
                'cedula',
                'edad',
                'genero',
                'correo',
                'telefono',
                ]

        
