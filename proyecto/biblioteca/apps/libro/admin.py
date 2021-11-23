from django.contrib import admin

# Register your models here.

from .models import Socios, clases, entrenador, actividad, salas, aparatos

admin.site.register(Socios)
admin.site.register(entrenador)
admin.site.register(actividad)
admin.site.register(salas)
admin.site.register(aparatos)
admin.site.register(clases)