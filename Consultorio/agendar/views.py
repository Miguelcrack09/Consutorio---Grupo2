from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import citasForm


def crud(request):
    return HttpResponse("Hola clase")

def miHtml(request):
    parametros=""
    return render(request, 'agendar.html')

def agendar(request):
    if request.method == "POST":
        form = citasForm(request.POST)
        if form.is_valid():
            creado = form.cleaned_data['nombre']
            messages.success(request, '¡Usuario registrado con exito!' )
            form.save()
            return redirect('http://localhost:8000/iniciosesion/html/')

    else:
        print("No es valido el post")
        form = citasForm() 

    context = {'form': form}
    return render(request, 'agendar.html')