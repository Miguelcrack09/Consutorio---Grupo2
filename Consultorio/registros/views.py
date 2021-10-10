from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario 

def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            creado = form.cleaned_data['nombre']
            messages.success(request, '¡Usuario registrado con exito!' )
            form.save()
            return redirect('http://localhost:8000/iniciosesion/html/')

    else:
        print("No es valido el post")
        form = UsuarioForm()

    context = {'form': form}
    return render(request, 'registros.html', context)

def eliminar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect("inicio")

