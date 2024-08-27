from django.contrib import admin
from .models import TituloProfesional, Profesor, Familia, Curso, Alumno, Materia, Tutor

@admin.register(TituloProfesional)
class TituloProfesionalAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'observacion')
    search_fields = ('denominacion',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'cuil', 'tel', 'f_nacimiento', 'get_titulos')
    search_fields = ('apellidos', 'nombres', 'cuil')
    list_filter = ('titulos',)

    def get_titulos(self, obj):
        return ', '.join([titulos.denominacion for titulos in obj.titulos.all()])
    get_titulos.short_description = 'títulos'    
    

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'titular')
    search_fields = ('apellidos',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('año', 'color')
    search_fields = ('año', 'color')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'dni', 'tel', 'familia', 'tutor', 'curso')
    search_fields = ('apellidos', 'nombres', 'dni')
    list_filter = ('curso',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'profesor_titular', 'profesor_interino')
    search_fields = ('denominacion',)
    list_filter = ('profesor_titular', 'profesor_interino')

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'dni', 'tel', 'familia', 'campo')
    search_fields = ('apellidos', 'nombres', 'dni')
    list_filter = ('familia',)
admin.site.site_header = 'Colegio Sagrado Corazón'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Administración del Colegio'