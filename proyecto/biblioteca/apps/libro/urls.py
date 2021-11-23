from django.urls import *
from .views import *

urlpatterns = [
    path('',inicio, name='index' ),
    path('aparatos/',Home, name='aparatos' ),
    path('salas/',Home1, name='salas' ),
    path('Socios/',Home2, name='Socios' ),
    path('entrenador/',Home3, name='entrenador' ),
    path('clases/',Home4, name='clases' ),
    path('actividad/',Home5, name='actividad'),
    path('clase_socio/',Home6, name='clase_socio'),
    path('entrenador_tipoactividad/',Home7, name='entrenador_actividad'),


]