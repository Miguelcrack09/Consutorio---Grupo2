from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.registro, name="Mi primera Html"),
    #path("eliminar/<int:usuario_id>/", views.eliminar, name=views.eliminar)
]