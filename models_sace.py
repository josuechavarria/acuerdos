# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AlumnosAlumno(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    persona = models.ForeignKey('CuentasPersona', unique=True)
    centro = models.ForeignKey('SecretariaCentroeducativo', blank=True, null=True)
    padre = models.ForeignKey('AlumnosPadrefamilia', blank=True, null=True)
    madre = models.ForeignKey('AlumnosPadrefamilia', blank=True, null=True)
    encargado = models.ForeignKey('AlumnosPadrefamilia', blank=True, null=True)
    problemas_salud = models.CharField(max_length=200, blank=True)
    observaciones = models.CharField(max_length=200, blank=True)
    bono_diezmil = models.IntegerField()
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    condicion_inicial = models.IntegerField()
    curso_prebasica = models.IntegerField(db_column='curso_preBasica')  # Field name made lowercase.
    jornada = models.ForeignKey('SecretariaJornada', blank=True, null=True)
    distancia_cc = models.IntegerField()
    ingreso_familiar = models.IntegerField()
    calzado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos_alumno'


class AlumnosAsistencia(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    matricula = models.ForeignKey('AlumnosMatricula')
    fecha = models.DateField()
    asistencia = models.BooleanField()
    motivo = models.IntegerField(blank=True, null=True)
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos_asistencia'


class AlumnosClaseconocimiento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    matricula = models.ForeignKey('AlumnosMatricula')
    nota_aprobar = models.IntegerField()
    nota_obtenida = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumnos_claseconocimiento'


class AlumnosClaseintensiva(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    matricula = models.ForeignKey('AlumnosMatricula')
    docente = models.ForeignKey('DocenteDocente')
    nota_aprobatoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumnos_claseintensiva'


class AlumnosClaseretrasada(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    matricula = models.ForeignKey('AlumnosMatricula')
    docente = models.ForeignKey('DocenteDocente')
    nota_aprobatoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumnos_claseretrasada'


class AlumnosClasesmatricularepitencia(models.Model):
