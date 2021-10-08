from django.shortcuts import render
from django.http import HttpResponse

def menucita(request):
    parametros=""
    return render(request, 'menucita.html')
 