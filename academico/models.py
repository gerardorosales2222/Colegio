from django.db import models

class TituloProfesional(models.Model):
    denominacion = models.CharField(max_length=100)
    observacion = models.TextField(null=True)
    def __str__(self):
        return '%s - %s '%(self.id,self.denominacion)
    class Meta:
        db_table = 'titulos_profes'
        verbose_name = 'titulo'
        verbose_name_plural = 'titulos de profes'

class Profesor(models.Model):
    apellidos = models.CharField(max_length=100, null=True)
    nombres = models.CharField(max_length=100, null=True)
    cuil = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    f_nacimiento = models.DateField(null=True)
    titulos = models.ManyToManyField(TituloProfesional, blank=False)
    def __str__(self):
        return '%s %s '%(self.apellidos,self.nombres)
    class Meta:
        db_table = 'profesores'
        verbose_name = 'profesor'
        verbose_name_plural = 'profesores'    
    
class Familia(models.Model):
    apellidos = models.CharField(max_length=100,null=True)
    titular = models.ForeignKey(Profesor, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'familias'
        verbose_name = 'familia'
        verbose_name_plural = 'familias'
    
class Curso(models.Model):
    año = [('1ro', 'Primer año'),('2do', 'Segundo año'),('3ro', 'Tercer año'),('4to', 'Cuarto año'),('5to', 'Quinto año'),]
    color = [('Am', 'Amarillo'),('V', 'Verde'),('R', 'Rojo'),('Az', 'Azul'),]
    def __str__(self):
        return '%s %s '%(self.año,self.color)
    class Meta:
        db_table = 'cursos'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

class Alumno(models.Model):
    apellidos = models.CharField(max_length=100, null=True)
    nombres = models.CharField(max_length=100, null=True)
    dni = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    class Meta:
        db_table = 'alumnos'
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

class Materia(models.Model):
    denominacion = models.CharField(max_length=100, null=True)
    profesor_titular = models.ForeignKey(Profesor, related_name='titular', null=True, on_delete=models.CASCADE)
    profesor_interino = models.ForeignKey(Profesor, related_name='interino', null=True, on_delete=models.CASCADE)
    class Meta:
        db_table = 'materias'
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
        
class Tutor(models.Model):
    apellidos = models.CharField(max_length=100, null=True)
    nombres = models.CharField(max_length=100, null=True)
    dni = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    campo = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s '%(self.apellidos,self.nombres)
    class Meta:
        db_table = 'tutores'
        verbose_name = 'tutor'
        verbose_name_plural = 'tutores'