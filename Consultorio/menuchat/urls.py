from django.urls import path 
from . import views

urlpatterns=[
    path("", views.menuchat, name="Menu Chat")
    
]