from django import forms

class Regform(forms.Form):
    OPTIONS = (    
            ("F", "Femenino"),
            ("M", "Masculino"),
            ("OTHER", "Otro"),
            )
            
    nombre = forms.CharField(max_length=45)
    apellido = forms.CharField(max_length=45)
    cedula = forms.IntegerField()
    edad = forms.IntegerField()
    genero = forms.ChoiceField(choices=OPTIONS)
    telefono = forms.CharField(max_length=45)
    correo = forms.EmailField()
    contraseña= forms.CharField(max_length=50)

