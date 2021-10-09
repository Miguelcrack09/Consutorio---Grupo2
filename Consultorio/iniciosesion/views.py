from django.shortcuts import render
from django.http import HttpResponse


# def inicio(request):
#     parametros=""
#     return HttpResponse("Hola clase")


def html(request):
     parametros = ""
     return render(request, "inicio.html")
# Create your views here.


def index(request):
    return HttpResponse("HOla ")