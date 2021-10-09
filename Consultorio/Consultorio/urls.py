from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', include('registros.urls')),
    path('iniciosesion/', include('iniciosesion.urls')),
    path('salaespera/', include('salaespera.urls')),
<<<<<<< Updated upstream
    path('menucita/', include ('menucita.urls')),
    path('menuchat/', include ('menuchat.urls'))
=======
    path('agendar/', include('agendar.urls'))
>>>>>>> Stashed changes
]
 