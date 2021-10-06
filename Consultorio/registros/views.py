from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola clase")

def miHtml(request):
    parametros=""
    return render(request, 'registros.html')

 