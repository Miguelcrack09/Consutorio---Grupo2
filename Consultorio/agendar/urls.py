from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.agendar, name="Mi primera Html"),
    path('crud/', views.crud, name="Crud"),
]