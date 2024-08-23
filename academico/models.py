from django.db import models

class Profesor(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=40, null=False, verbose_name='Apellido')
    cuil = models.CharField(max_length=11, null=False, verbose_name='CUIL')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

class Materia(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return '%s '%(self.nombre)  
    class Meta:
        db_table = 'Materia'
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

""""
class Alumno(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    materias = models.ManyToManyField(Materias, blank=False)
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Alumno'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
"""