from django.shortcuts import render
from django.http import HttpResponse

def menuchat(request):
    return render(request, 'menuchat.html')
 
