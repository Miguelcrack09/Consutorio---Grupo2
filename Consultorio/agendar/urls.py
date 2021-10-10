from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendar/', views.miHtml, name="Mi primera Html"),
    path('crud/', views.crud, name="Crud"),
]