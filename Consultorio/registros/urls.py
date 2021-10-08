from django.urls import path
from . import views

urlpatterns = [
    path("", views.miHtml, name="Mi primera Html"),
]