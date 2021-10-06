from django.urls import path
from . import views

urlpatterns = [
    path("miHtml/", views.miHtml, name="Mi primera Html"),
]