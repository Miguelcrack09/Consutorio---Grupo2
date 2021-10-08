from django.shortcuts import render
from django.http import HttpResponse
from .forms import Regform
from .models import Usuario

def hola(request):
    return HttpResponse("Hola clase")

def miHtml(request):
    form = Regform(request.POST )
    if form.is_valid():
        form_data = form.cleaned_data
        print ("Deberia aparecer algo aqui...2ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11111")
        abc = form_data.get("nombre")
        abd = form_data.get("apellido")
        print ("Deberia aparecer algo aqui...2ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"+abc)
        obj = Usuario.objects.create(nombre=abc, apellido=abd)
        print (obj)
        
    context = {
        "form": form,
    }
    parametros=""
    return render(request, 'registros.html', context)

 