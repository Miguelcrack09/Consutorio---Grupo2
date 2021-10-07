from django.urls import path, include
from . import views

urlpatterns = [
    path('wait/', views.waitf, name='wait url'),
]