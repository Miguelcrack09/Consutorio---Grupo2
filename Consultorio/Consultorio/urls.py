from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', include('registros.urls')),
<<<<<<< HEAD
    path('iniciosesion/', include('iniciosesion.urls')),
=======
    path('salaespera/', include('salaespera.urls')),
>>>>>>> 2dbd47e6c5b5bd5de2b1939ae4b5ea170eb6fcc8
]
