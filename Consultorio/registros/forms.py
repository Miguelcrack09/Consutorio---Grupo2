from django import forms

class Regform(forms.Form):
    OPTIONS = (    
            ("F", "Femenino"),
            ("M", "Masculino"),
            ("OTHER", "Otro"),
            )
            
    nombre = forms.CharField(max_length=45)
    apellido = forms.CharField(max_length=45)
    edad = forms.IntegerField()
    genero = forms.ChoiceField(choices=OPTIONS)
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=45)
    rol = forms.CharField(max_length=45)

