from django.db import models
from django.db.models.base import Model


# Create your models here.

class Socios(models.Model):
    DniS = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellido = models.CharField(max_length=200, blank= False, null=False)
    telefono = models.CharField(blank= False, null=False, max_length=20)
    profesion= models.CharField(max_length=200, blank=False, null=False)
    CBU = models.CharField(max_length=150, blank=False, null=False)
    direcciòn= models.CharField(max_length=200, blank= False, null=False)

    class meta:
        verbose_name='socio'
        verbose_name_plural='socios'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre

class clases(models.Model):
    Codigo_clas = models.AutoField(primary_key=True)        
    dia = models.DateTimeField(max_length=100, blank=False, null=False)
    hora = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name='clases'
        verbose_name_plural='clases'
        ordering=['dia']
    
    def __str__(self):
        return self.dia


class entrenador(models.Model):
    dni = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    telefono = models.IntegerField(blank=False, null=False, max_length=20)
    experiencia = models.CharField(max_length=200, blank=False, null=False)
    titulacion= models.CharField(max_length=150, blank=False, null=False)
    Codigo_clase = models.ForeignKey(clases, on_delete=models.CASCADE)

    class meta:
        verbose_name= 'entrenador'
        verbose_name_plural= 'entrenadores'
        ordering= ['nombre']
    
    def __str__(self):
        return self.nombre
    

class actividad(models.Model):
    ID_actividad = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name='actividad'
        verbose_name_plural='actividades'
        ordering=['descripcion']
    
    def __str__(self):
        return self.descripcion
    

class aparatos(models.Model):
    codigoA = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name='aparatos'
        verbose_name_plural='aparatos'
        ordering=['estado']
    
    def __str__(self):
        return self.estado

class salas(models.Model):
    numeroS = models.AutoField(primary_key=True)
    metros = models.CharField(max_length=200, blank=False, null=False)
    tipo = models.CharField(max_length=100, blank= False, null= False)
    ubicacion = models.CharField(max_length=120, blank=False, null=False)
    Codigo_clas = models.ForeignKey(clases, on_delete=models.CASCADE)
    codigoA = models.ForeignKey(aparatos, on_delete=models.CASCADE)

    class Meta:
        verbose_name='salas'
        verbose_name_plural='salas'
        ordering=['metros']
    
    def __str__(self):
        return self.metros

class clases_socios(models.Model):
    Codigoclas = models.ForeignKey(clases, on_delete=models.CASCADE)
    dni_socio = models.ForeignKey(Socios, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name='clases_socios'
        verbose_name_plural='clases_socios'
        ordering=['descripcion']
    
    def __str__(self):
        return self.descripcion

class entrenador_tipoactividad(models.Model):
    Dni_e = models.ForeignKey(entrenador, on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(actividad, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name='entrenador_tipoactividad'
        verbose_name_plural='entrenador_tipodeactividades'
        ordering=['descripcion']
    
    def __str__(self):
        return self.descripcion