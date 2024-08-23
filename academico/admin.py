from django.contrib import admin
from .models import *

@admin.register(Profesor)
class profesor(admin.ModelAdmin):
    list_display = ('id', 'dni', 'nombre', 'apellido', 'tel')
"""
@admin.register(Alumno)
class alumno(admin.ModelAdmin):
    list_display = ('id', 'dni', 'nombre', 'apellido', 'tel','get_materias')

    def get_materias(self, obj):
        return ', '.join([Materia.nombre for Carrera in obj.Materia.all()])
"""

admin.site.register(Materia)


admin.site.site_header = 'Colegio Sagrado Corazón'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Administración del Colegio'