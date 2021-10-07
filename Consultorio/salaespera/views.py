from django.shortcuts import render
from django.http import HttpResponse

def waitf(request):
    parametros=""
    return render(request, 'wait.html')