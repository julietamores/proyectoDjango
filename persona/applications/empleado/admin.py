from django.contrib import admin
from .models import Empleado, Habilidad

# Register your models here.
class EmpleadoAdmin (admin.ModelAdmin): 
    list_display = (
        'apellidos',
        'nombres',
        'nombre_completo',
        'dni',
        'area',
        'habilidades',
    )

    search_fields = ('apellidos',)
    list_filter = ('area', 'hablidades',)


admin.site.register(Empleado)
admin.site.register(Habilidad)
