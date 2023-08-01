from django.db import models

# Create your models here.

class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    cedula_identidad= models.IntegerField(unique=True)
    correo = models.EmailField(max_length=300)
    contrasena = models.CharField(max_length=150)
    rol = models.CharField(max_length=60)
    estado = models.CharField(max_length=3, default='A')

class Asignatura(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=200)
    objetivo_asignatura = models.CharField(max_length=650)
    aportes_teoricos = models.CharField(max_length=1500)
    objetivos_especificos = models.CharField(max_length=1500)
    producto_academico = models.CharField(max_length=1500)
    prerequisito_academico = models.CharField(max_length=400)
    periodo = models.CharField(max_length=150)
    estado = models.CharField(max_length=3, default='A')

class Referencias(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_referencia = models.CharField(max_length=100)
    numero_referencia = models.IntegerField()
    titulo_obra = models.CharField(max_length=500)
    existencia_biblioteca = models.CharField(max_length=450)
    numero_ejemplares = models.IntegerField()
    estado = models.CharField(max_length=3, default='A')

class ProductoAcademico(models.Model):
    id = models.IntegerField(primary_key=True)
    producto_final = models.CharField(max_length=500)
    objetivo = models.TextField()
    producto_parcial = models.TextField()
    presentacion = models.TextField()
    integracion = models.TextField()
    estado = models.CharField(max_length=3, default='A')

