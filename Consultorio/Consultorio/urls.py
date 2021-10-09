from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    
    path('registros/', include('registros.urls')),
    path('iniciosesion/', include('iniciosesion.urls')),
    path('salaespera/', include('salaespera.urls')),
    path('admin/', admin.site.urls),
    #path('citas/', include('citas.urls')),
]
 