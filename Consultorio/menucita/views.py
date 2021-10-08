from django.shortcuts import render
from django.http import HttpResponse

def menucita(request):
    return render(request, 'menucita.html')
 