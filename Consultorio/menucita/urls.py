from django.urls import path 
from . import views

urlpatterns=[
    path("", views.menucita, name="Primer Menu")
    
]