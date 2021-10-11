from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import citasForm
from .models import Citas


def crud(request):
    return HttpResponse("Hola clase")

def miHtml(request):
    parametros=""
    return render(request, 'agendar.html')

def agendar(request):
    print("Entra a agendar")
    #variable = Citas.objects.all()
    #variable.get()
    if request.method == "POST":
        print("request.method: "+request.method)
        form = citasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/iniciosesion/')

    else:
        print("request: "+request.method)
        form = citasForm() 
        pass

    context = {'form': form}
    return render(request, 'agendar.html', context)