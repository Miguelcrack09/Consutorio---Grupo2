from django.urls import path
from . import views

urlpatterns = [
    #path("inicio/", views.inicio, name="INICIO"),
    path("", views.html, name = "Inicio sesion"),
    # path('', views.index, name='index'),
]