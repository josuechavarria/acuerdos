# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AlumnosAlumno(models.Model):
    id = models.IntegerField(primary_key=True)
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
    curso_prebasica = models.IntegerField(db_column='curso_preBasica') # Field name made lowercase.
    jornada = models.ForeignKey('SecretariaJornada', blank=True, null=True)
    distancia_cc = models.IntegerField()
    ingreso_familiar = models.IntegerField()
    calzado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_alumno'

class AlumnosAsistencia(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    nota_aprobar = models.IntegerField()
    nota_obtenida = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'alumnos_claseconocimiento'

class AlumnosClaseintensiva(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    docente = models.ForeignKey('DocenteDocente')
    nota_aprobatoria = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'alumnos_claseintensiva'

class AlumnosClaseretrasada(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    docente = models.ForeignKey('DocenteDocente')
    nota_aprobatoria = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'alumnos_claseretrasada'

class AlumnosEquivalencia(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    class Meta:
        managed = False
        db_table = 'alumnos_equivalencia'

class AlumnosFaltadisciplinariaalumno(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    falta = models.ForeignKey('CentroeducativoFaltadisciplinaria')
    class Meta:
        managed = False
        db_table = 'alumnos_faltadisciplinariaalumno'

class AlumnosInasistencia(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey('AlumnosMatricula')
    total_dias = models.SmallIntegerField()
    parcial = models.ForeignKey('CentroeducativoParcial')
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_inasistencia'

class AlumnosLogalumnoeliminado(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey('AuthUser')
    identidad = models.CharField(max_length=15)
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    class Meta:
        managed = False
        db_table = 'alumnos_logalumnoeliminado'

class AlumnosLogmatriculaeliminada(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey('AuthUser')
    identidad = models.CharField(max_length=15)
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    periodo = models.CharField(max_length=4)
    centro_id = models.IntegerField()
    grado_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'alumnos_logmatriculaeliminada'

class AlumnosMatricula(models.Model):
    id = models.IntegerField(primary_key=True)
    alumno = models.ForeignKey(AlumnosAlumno)
    seccion = models.ForeignKey('CentroeducativoSeccion')
    estado = models.IntegerField()
    fecha = models.DateField()
    observaciones = models.CharField(max_length=255, blank=True)
    fecha_cancelada = models.DateField(blank=True, null=True)
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    razones_cancelada = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_matricula'

class AlumnosPadrefamilia(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey('CuentasPersona', unique=True)
    ocupacion = models.CharField(max_length=100, blank=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True)
    telefono_trabajo = models.CharField(max_length=8, blank=True)
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_padrefamilia'

class AlumnosProgramStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    program = models.ForeignKey('SecretariaBeneficalprograms')
    student = models.ForeignKey(AlumnosAlumno)
    class Meta:
        managed = False
        db_table = 'alumnos_program_student'

class AlumnosResumenAsistencia(models.Model):
    id = models.IntegerField(primary_key=True)
    parcial = models.ForeignKey('CentroeducativoParcial')
    matricula = models.ForeignKey(AlumnosMatricula)
    total_dias = models.SmallIntegerField()
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_resumen_asistencia'

class AlumnosResumenasistencia(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.ForeignKey('CentroeducativoPeriodoclases')
    matricula = models.ForeignKey(AlumnosMatricula)
    total_dias = models.SmallIntegerField()
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_resumenasistencia'

class AlumnosStudentPersonality(models.Model):
    id = models.IntegerField(primary_key=True)
    registration = models.ForeignKey(AlumnosMatricula)
    opt1 = models.IntegerField()
    opt2 = models.IntegerField()
    opt3 = models.IntegerField()
    opt4 = models.IntegerField()
    opt5 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'alumnos_student_personality'

class AlumnosTraslado(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.ForeignKey(AlumnosMatricula)
    centro_destino = models.ForeignKey('SecretariaCentroeducativo')
    fecha_solicitado = models.DateField()
    fecha_confirmado = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True)
    matricula_destino = models.ForeignKey(AlumnosMatricula, blank=True, null=True)
    estado = models.IntegerField()
    usuario_creador = models.ForeignKey('AuthUser', blank=True, null=True)
    usuario_modifico = models.ForeignKey('AuthUser', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'alumnos_traslado'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser')
    message = models.TextField()
    class Meta:
        managed = False
        db_table = 'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class BeneficiosAlumnoPreplanillaPlanilla(models.Model):
    id = models.IntegerField(primary_key=True)
    departamento = models.CharField(max_length=2)
    municipio = models.CharField(max_length=2)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=128)
    anio = models.CharField(max_length=6)
    codigo_beneficio = models.CharField(max_length=2)
    nivel_educativo = models.CharField(max_length=4)
    no_identidad = models.CharField(max_length=13)
    primer_apellido = models.CharField(max_length=32)
    segundo_apellido = models.CharField(max_length=32, blank=True)
    primer_nombre = models.CharField(max_length=32)
    segundo_nombre = models.CharField(max_length=32, blank=True)
    grado = models.CharField(max_length=64, blank=True)
    seccion = models.CharField(db_column='Seccion', max_length=64, blank=True) # Field name made lowercase.
    indice = models.CharField(max_length=3, blank=True)
    monto_pagado = models.FloatField()
    sexo = models.CharField(max_length=1, blank=True)
    repitente = models.CharField(max_length=1, blank=True)
    modalidad = models.CharField(max_length=3, blank=True)
    jornada = models.CharField(max_length=32, blank=True)
    no_clases_retrazadas = models.CharField(max_length=2, blank=True)
    codigo_rango = models.CharField(max_length=2, blank=True)
    no_solicitud = models.CharField(max_length=6, blank=True)
    no_planilla = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.ForeignKey(AuthUser)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(AuthUser, blank=True, null=True)
    es_planilla = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'beneficios_alumno_preplanilla_planilla'

class BeneficiosBeneficioACentro(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_beneficio_nivel = models.ForeignKey('BeneficiosBeneficionivel')
    codigo_centro = models.ForeignKey('SecretariaCentroeducativo')
    codigo_periodo = models.ForeignKey('BeneficiosPeriodo')
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.ForeignKey(AuthUser)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(AuthUser, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'beneficios_beneficio_a_centro'

class BeneficiosBeneficionivel(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_beneficio = models.ForeignKey('BeneficiosTipobeneficio')
    nivel_educativo = models.ForeignKey('SecretariaNiveleducativo')
    monto_asignado = models.FloatField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.ForeignKey(AuthUser)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(AuthUser, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'beneficios_beneficionivel'

class BeneficiosHistobeneficios(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_planilla = models.CharField(max_length=10)
    departamento = models.ForeignKey('SecretariaDepartamento')
    municipio = models.ForeignKey('SecretariaMunicipio')
    codigo_plantel = models.IntegerField()
    codigo_centro = models.CharField(max_length=9)
    descripcion_centro = models.CharField(max_length=256, blank=True)
    anio = models.CharField(max_length=6)
    codigo_beneficio = models.ForeignKey('BeneficiosTipobeneficios')
    nivel_educativo = models.ForeignKey('SecretariaNiveleducativo')
    no_identidad = models.CharField(max_length=13)
    primer_apellido = models.CharField(max_length=32)
    segundo_apellido = models.CharField(max_length=32, blank=True)
    primer_nombre = models.CharField(max_length=32)
    segundo_nombre = models.CharField(max_length=32, blank=True)
    grado = models.CharField(max_length=2, blank=True)
    indice = models.CharField(max_length=3, blank=True)
    no_cheque = models.CharField(max_length=8, blank=True)
    monto_cheque = models.FloatField()
    prefijo_cheque = models.CharField(max_length=2)
    anio_cheque = models.CharField(max_length=6)
    tipo_planilla = models.CharField(max_length=2, blank=True)
    validacion = models.CharField(max_length=2, blank=True)
    sexo = models.CharField(max_length=1, blank=True)
    repitente = models.CharField(max_length=1, blank=True)
    modalidad = models.CharField(max_length=3, blank=True)
    descripcion_modalidad = models.CharField(max_length=256, blank=True)
    jornada = models.CharField(max_length=1, blank=True)
    seccion = models.CharField(db_column='Seccion', max_length=3, blank=True) # Field name made lowercase.
    retrazada = models.CharField(max_length=2, blank=True)
    no_planilla = models.CharField(max_length=2, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=15, blank=True)
    fecha_modificacion = models.CharField(max_length=255, blank=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True)
    codigo_rango = models.CharField(max_length=2, blank=True)
    no_solicitud = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'beneficios_histobeneficios'

class BeneficiosHistotipobeneficios(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_beneficio = models.CharField(max_length=2)
    descripcion_beneficio = models.CharField(max_length=255)
    abreviacion_beneficio = models.CharField(max_length=5, blank=True)
    monto_beneficio = models.FloatField(blank=True, null=True)
    nota_minima = models.CharField(max_length=3)
    prefijo_cheque = models.CharField(max_length=2)
    bloqueo_posteo = models.CharField(max_length=2, blank=True)
    monto_asignado = models.FloatField(blank=True, null=True)
    monto_ejecutado = models.FloatField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=15, blank=True)
    fecha_modificacion = models.CharField(max_length=255, blank=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'beneficios_histotipobeneficios'

class BeneficiosPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_periodo = models.CharField(unique=True, max_length=6)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.ForeignKey(AuthUser)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(AuthUser, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'beneficios_periodo'

class BeneficiosTipobeneficio(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_beneficio = models.CharField(unique=True, max_length=2)
    descripcion_beneficio = models.CharField(max_length=255)
    abreviacion_beneficio = models.CharField(max_length=5, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.ForeignKey(AuthUser)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(AuthUser, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'beneficios_tipobeneficio'

class BeneficiosTipobeneficios(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_beneficio = models.CharField(max_length=2)
    descripcion_beneficio = models.CharField(max_length=255)
    abreviacion_beneficio = models.CharField(max_length=5, blank=True)
    monto_beneficio = models.FloatField(blank=True, null=True)
    nota_minima = models.CharField(max_length=3)
    prefijo_cheque = models.CharField(max_length=2)
    bloqueo_posteo = models.CharField(max_length=2, blank=True)
    monto_asignado = models.FloatField(blank=True, null=True)
    monto_ejecutado = models.FloatField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=15, blank=True)
    fecha_modificacion = models.CharField(max_length=255, blank=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'beneficios_tipobeneficios'

class CentroeducativoClasecentro(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    multihorario = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'centroeducativo_clasecentro'

class CentroeducativoClasemalla(models.Model):
    id = models.IntegerField(primary_key=True)
    malla_curricular = models.ForeignKey('CentroeducativoMallacurricular')
    clase = models.ForeignKey(CentroeducativoClasecentro)
    class Meta:
        managed = False
        db_table = 'centroeducativo_clasemalla'

class CentroeducativoClaseseccion(models.Model):
    id = models.IntegerField(primary_key=True)
    seccion = models.ForeignKey('CentroeducativoSeccion')
    plaza = models.ForeignKey('DocentePlaza', blank=True, null=True)
    nota_aprobatoria = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType')
    object_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'centroeducativo_claseseccion'

class CentroeducativoFaltadisciplinaria(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=3)
    descripcion = models.CharField(max_length=128)
    class Meta:
        managed = False
        db_table = 'centroeducativo_faltadisciplinaria'

class CentroeducativoHorario(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    jornada = models.ForeignKey('SecretariaJornada')
    periodo = models.ForeignKey('CentroeducativoPeriodoclases')
    descripcion = models.CharField(max_length=100)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_horario'

class CentroeducativoHorarioHora(models.Model):
    id = models.IntegerField(primary_key=True)
    horario = models.ForeignKey(CentroeducativoHorario)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    class Meta:
        managed = False
        db_table = 'centroeducativo_horario_hora'

class CentroeducativoHorarioclaseseccion(models.Model):
    id = models.IntegerField(primary_key=True)
    clase_seccion = models.ForeignKey(CentroeducativoClaseseccion)
    hora = models.ForeignKey(CentroeducativoHorarioHora)
    dia = models.IntegerField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_horarioclaseseccion'

class CentroeducativoMallacurricular(models.Model):
    id = models.IntegerField(primary_key=True)
    anio = models.IntegerField()
    centro = models.ForeignKey('SecretariaCentroeducativo')
    malla_oficial = models.ForeignKey('SecretariaMallacurricularoficial')
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_mallacurricular'

class CentroeducativoParcial(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.ForeignKey('CentroeducativoPeriodoclases')
    nombre = models.CharField(max_length=128)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_parcial'

class CentroeducativoPeriodoclases(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    descripcion = models.CharField(max_length=128)
    inicio_periodo = models.DateField()
    final_periodo = models.DateField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_periodoclases'

class CentroeducativoProgramInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    program = models.ForeignKey('SecretariaBeneficalprograms')
    institution = models.ForeignKey('SecretariaCentroeducativo')
    class Meta:
        managed = False
        db_table = 'centroeducativo_program_institution'

class CentroeducativoRecuperacion(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.ForeignKey(CentroeducativoPeriodoclases)
    descripcion = models.CharField(max_length=128)
    fecha = models.DateField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_recuperacion'

class CentroeducativoSeccion(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    periodo_clases = models.ForeignKey(CentroeducativoPeriodoclases)
    jornada = models.ForeignKey('SecretariaJornada')
    malla_curricular = models.ForeignKey(CentroeducativoMallacurricular)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'centroeducativo_seccion'

class CentroeducativoVotoelectronico(models.Model):
    id = models.IntegerField(primary_key=True)
    alumno_votante = models.ForeignKey(AlumnosMatricula, unique=True)
    fecha = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'centroeducativo_votoelectronico'

class CentroeducativoVotoscandidato(models.Model):
    id = models.IntegerField(primary_key=True)
    alumno_candidato = models.ForeignKey(AlumnosMatricula, unique=True)
    cantidad_votos = models.IntegerField()
    movimiento = models.CharField(max_length=64)
    lema = models.CharField(max_length=128)
    class Meta:
        managed = False
        db_table = 'centroeducativo_votoscandidato'

class CmsCmsplugin(models.Model):
    id = models.IntegerField(primary_key=True)
    placeholder = models.ForeignKey('CmsPlaceholder', blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)
    language = models.CharField(max_length=15)
    plugin_type = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    level = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'cms_cmsplugin'

class CmsGlobalpagepermission(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, blank=True, null=True)
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_moderate = models.BooleanField()
    can_view = models.BooleanField()
    can_recover_page = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission'

class CmsGlobalpagepermissionSites(models.Model):
    id = models.IntegerField(primary_key=True)
    globalpagepermission = models.ForeignKey(CmsGlobalpagepermission)
    site = models.ForeignKey('DjangoSite')
    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission_sites'

class CmsPage(models.Model):
    id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=70)
    changed_by = models.CharField(max_length=70)
    parent = models.ForeignKey('self', blank=True, null=True)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    publication_date = models.DateTimeField(blank=True, null=True)
    publication_end_date = models.DateTimeField(blank=True, null=True)
    in_navigation = models.BooleanField()
    soft_root = models.BooleanField()
    reverse_id = models.CharField(max_length=40, blank=True)
    navigation_extenders = models.CharField(max_length=80, blank=True)
    published = models.BooleanField()
    template = models.CharField(max_length=100)
    site = models.ForeignKey('DjangoSite')
    moderator_state = models.SmallIntegerField()
    level = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    login_required = models.BooleanField()
    limit_visibility_in_menu = models.SmallIntegerField(blank=True, null=True)
    publisher_is_draft = models.BooleanField()
    publisher_public = models.ForeignKey('self', unique=True, blank=True, null=True)
    publisher_state = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'cms_page'

class CmsPagePlaceholders(models.Model):
    id = models.IntegerField(primary_key=True)
    page = models.ForeignKey(CmsPage)
    placeholder = models.ForeignKey('CmsPlaceholder')
    class Meta:
        managed = False
        db_table = 'cms_page_placeholders'

class CmsPagemoderator(models.Model):
    id = models.IntegerField(primary_key=True)
    page = models.ForeignKey(CmsPage)
    user = models.ForeignKey(AuthUser)
    moderate_page = models.BooleanField()
    moderate_children = models.BooleanField()
    moderate_descendants = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'cms_pagemoderator'

class CmsPagemoderatorstate(models.Model):
    id = models.IntegerField(primary_key=True)
    page = models.ForeignKey(CmsPage)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    created = models.DateTimeField()
    action = models.CharField(max_length=3, blank=True)
    message = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_pagemoderatorstate'

class CmsPagepermission(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, blank=True, null=True)
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_moderate = models.BooleanField()
    can_view = models.BooleanField()
    grant_on = models.IntegerField()
    page = models.ForeignKey(CmsPage, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cms_pagepermission'

class CmsPageuser(models.Model):
    user_ptr = models.ForeignKey(AuthUser, primary_key=True)
    created_by = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'cms_pageuser'

class CmsPageusergroup(models.Model):
    group_ptr = models.ForeignKey(AuthGroup, primary_key=True)
    created_by = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'cms_pageusergroup'

class CmsPlaceholder(models.Model):
    id = models.IntegerField(primary_key=True)
    slot = models.CharField(max_length=50)
    default_width = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cms_placeholder'

class CmsTitle(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    menu_title = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    has_url_overwrite = models.BooleanField()
    application_urls = models.CharField(max_length=200, blank=True)
    redirect = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    page_title = models.CharField(max_length=255, blank=True)
    page = models.ForeignKey(CmsPage)
    creation_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'cms_title'

class CmspluginCalendarentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cmsplugin_calendarentriesplugin'

class CmspluginFile(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    file = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'cmsplugin_file'

class CmspluginGooglemap(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    zoom = models.SmallIntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    route_planer_title = models.CharField(max_length=150, blank=True)
    route_planer = models.BooleanField()
    width = models.CharField(max_length=6)
    height = models.CharField(max_length=6)
    class Meta:
        managed = False
        db_table = 'cmsplugin_googlemap'

class CmspluginLatestentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    subcategories = models.BooleanField()
    number_of_entries = models.IntegerField()
    template_to_render = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'cmsplugin_latestentriesplugin'

class CmspluginLatestnewsplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    limit = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'cmsplugin_latestnewsplugin'

class CmspluginLink(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=200, blank=True)
    page_link = models.ForeignKey(CmsPage, blank=True, null=True)
    mailto = models.CharField(max_length=75, blank=True)
    target = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'cmsplugin_link'

class CmspluginNewsNews(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=50)
    excerpt = models.TextField()
    content = models.TextField()
    is_published = models.BooleanField()
    pub_date = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    link = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'cmsplugin_news_news'

class CmspluginPicture(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    image = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    page_link = models.ForeignKey(CmsPage, blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True)
    longdesc = models.CharField(max_length=255, blank=True)
    float = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'cmsplugin_picture'

class CmspluginQueryentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    query = models.CharField(max_length=250)
    number_of_entries = models.IntegerField()
    template_to_render = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'cmsplugin_queryentriesplugin'

class CmspluginRandomentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    number_of_entries = models.IntegerField()
    template_to_render = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'cmsplugin_randomentriesplugin'

class CmspluginSelectedentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    template_to_render = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'cmsplugin_selectedentriesplugin'

class CmspluginSnippetptr(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    snippet = models.ForeignKey('SnippetSnippet')
    class Meta:
        managed = False
        db_table = 'cmsplugin_snippetptr'

class CmspluginText(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    body = models.TextField()
    class Meta:
        managed = False
        db_table = 'cmsplugin_text'

class CmspluginVideo(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, primary_key=True)
    movie = models.CharField(max_length=100, blank=True)
    movie_url = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=100, blank=True)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    auto_play = models.BooleanField()
    auto_hide = models.BooleanField()
    fullscreen = models.BooleanField()
    loop = models.BooleanField()
    bgcolor = models.CharField(max_length=6)
    textcolor = models.CharField(max_length=6)
    seekbarcolor = models.CharField(max_length=6)
    seekbarbgcolor = models.CharField(max_length=6)
    loadingbarcolor = models.CharField(max_length=6)
    buttonoutcolor = models.CharField(max_length=6)
    buttonovercolor = models.CharField(max_length=6)
    buttonhighlightcolor = models.CharField(max_length=6)
    class Meta:
        managed = False
        db_table = 'cmsplugin_video'

class CmspluginZinniaLatestentriespluginAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    latestentriesplugin = models.ForeignKey(CmspluginLatestentriesplugin)
    user = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'cmsplugin_zinnia_latestentriesplugin_authors'

class CmspluginZinniaLatestentriespluginCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    latestentriesplugin = models.ForeignKey(CmspluginLatestentriesplugin)
    category = models.ForeignKey('ZinniaCategory')
    class Meta:
        managed = False
        db_table = 'cmsplugin_zinnia_latestentriesplugin_categories'

class CmspluginZinniaLatestentriespluginTags(models.Model):
    id = models.IntegerField(primary_key=True)
    latestentriesplugin = models.ForeignKey(CmspluginLatestentriesplugin)
    tag = models.ForeignKey('TaggingTag')
    class Meta:
        managed = False
        db_table = 'cmsplugin_zinnia_latestentriesplugin_tags'

class CmspluginZinniaSelectedentriespluginEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    selectedentriesplugin = models.ForeignKey(CmspluginSelectedentriesplugin)
    entry = models.ForeignKey('ZinniaEntry')
    class Meta:
        managed = False
        db_table = 'cmsplugin_zinnia_selectedentriesplugin_entries'

class CuentasJerarquia(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = 'cuentas_jerarquia'

class CuentasJerarquiaCargo(models.Model):
    id = models.IntegerField(primary_key=True)
    jerarquia = models.ForeignKey(CuentasJerarquia)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'cuentas_jerarquia_cargo'

class CuentasPersona(models.Model):
    id = models.IntegerField(primary_key=True)
    identidad = models.CharField(max_length=20)
    tipoid = models.ForeignKey('SecretariaTipodocumentoid', db_column='tipoID_id') # Field name made lowercase.
    primer_nombre = models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60, blank=True)
    primer_apellido = models.CharField(max_length=60)
    segundo_apellido = models.CharField(max_length=60, blank=True)
    sexo = models.CharField(max_length=1)
    nacionalidad = models.ForeignKey('SecretariaPais')
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    domicilio = models.ForeignKey('SecretariaMunicipio')
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9, blank=True)
    lugar_nacimiento = models.CharField(max_length=150)
    correo = models.CharField(max_length=75)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cuentas_persona'

class CuentasPersonaimagen(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=100)
    persona = models.ForeignKey(CuentasPersona, unique=True)
    class Meta:
        managed = False
        db_table = 'cuentas_personaimagen'

class CuentasPersonalog(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(CuentasPersona)
    identidad = models.CharField(max_length=20)
    tipoid = models.ForeignKey('SecretariaTipodocumentoid', db_column='tipoID_id') # Field name made lowercase.
    primer_nombre = models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60, blank=True)
    primer_apellido = models.CharField(max_length=60)
    segundo_apellido = models.CharField(max_length=60, blank=True)
    sexo = models.CharField(max_length=1)
    nacionalidad = models.ForeignKey('SecretariaPais')
    fecha_nacimiento = models.DateTimeField()
    domicilio = models.ForeignKey('SecretariaMunicipio')
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9, blank=True)
    lugar_nacimiento = models.CharField(max_length=150, blank=True)
    correo = models.CharField(max_length=75, blank=True)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cuentas_personalog'

class CuentasUserCentroJornada(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(AuthUser)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    jornada = models.ForeignKey('SecretariaJornada')
    cargo_id = models.IntegerField()
    persona = models.ForeignKey(CuentasPersona)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cuentas_user_centro_jornada'

class CuentasUsuariosLogeados(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(AuthUser)
    ip = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'cuentas_usuarios_logeados'

class DepartamentalesDirecciondepartamental(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=10)
    departamento = models.ForeignKey('SecretariaDepartamento', unique=True)
    numero_telefonico = models.IntegerField()
    direccion = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'departamentales_direcciondepartamental'

class DepartamentalesDirectordepartamental(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(CuentasPersona, unique=True)
    fecha_ingreso = models.DateField()
    direccion_departamental = models.ForeignKey(DepartamentalesDirecciondepartamental)
    cargo = models.ForeignKey(AuthGroup, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'departamentales_directordepartamental'

class DistritalesDirecciondistrital(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=8)
    municipio = models.ForeignKey('SecretariaMunicipio')
    tipo_direccion = models.IntegerField()
    numero_telefonico = models.IntegerField()
    direccion = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'distritales_direcciondistrital'

class DistritalesDirecciondistritalCentroeducativo(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion_distrital_id = models.IntegerField()
    centro_educativo = models.ForeignKey('SecretariaCentroeducativo', unique=True)
    class Meta:
        managed = False
        db_table = 'distritales_direcciondistrital_centroeducativo'

class DistritalesDirectordistrital(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(CuentasPersona, unique=True)
    direccion_distrital_id = models.IntegerField()
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    cargo = models.ForeignKey(AuthGroup, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'distritales_directordistrital'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoCommentFlags(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    comment = models.ForeignKey('DjangoComments')
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_comment_flags'

class DjangoComments(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey('DjangoContentType')
    object_pk = models.TextField()
    site = models.ForeignKey('DjangoSite')
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=75)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'django_comments'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class DocenteDocente(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(CuentasPersona, unique=True)
    codigoihss = models.CharField(db_column='codigoIHSS', max_length=32, blank=True) # Field name made lowercase.
    claveescalafon = models.CharField(db_column='claveEscalafon', max_length=32, blank=True) # Field name made lowercase.
    numerocolegiacion = models.CharField(db_column='numeroColegiacion', max_length=32, blank=True) # Field name made lowercase.
    numeroafiliacioninprema = models.CharField(db_column='numeroAfiliacionInprema', max_length=32, blank=True) # Field name made lowercase.
    especialidad = models.CharField(max_length=256, blank=True)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    porcontrato = models.NullBooleanField(db_column='porContrato') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'docente_docente'

class DocenteDocentecentro(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    docente = models.ForeignKey(DocenteDocente)
    class Meta:
        managed = False
        db_table = 'docente_docentecentro'

class DocenteDocentessiarhd(models.Model):
    id = models.IntegerField(primary_key=True)
    identidad = models.CharField(max_length=13, blank=True)
    clave_escalafon = models.CharField(max_length=128, blank=True)
    nombres_empleado = models.CharField(max_length=128, blank=True)
    apellidos_empleado = models.CharField(max_length=128, blank=True)
    sexo = models.CharField(max_length=128, blank=True)
    fecha_nacimiento = models.CharField(max_length=128, blank=True)
    class Meta:
        managed = False
        db_table = 'docente_docentessiarhd'

class DocenteDocentessiarhdc(models.Model):
    id = models.IntegerField(primary_key=True)
    identidad = models.CharField(max_length=13, blank=True)
    clave_escalafon = models.CharField(max_length=16, blank=True)
    class Meta:
        managed = False
        db_table = 'docente_docentessiarhdc'

class DocenteHistorialclasedocente(models.Model):
    id = models.IntegerField(primary_key=True)
    historial = models.ForeignKey('DocenteHistorialdocente')
    class Meta:
        managed = False
        db_table = 'docente_historialclasedocente'

class DocenteHistorialdocente(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    docente = models.ForeignKey(DocenteDocente)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'docente_historialdocente'

class DocentePlaza(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_plaza = models.CharField(max_length=6)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    jornada = models.ForeignKey('SecretariaJornada')
    docente = models.ForeignKey(DocenteDocente, blank=True, null=True)
    fecha_ocupacion = models.DateField(blank=True, null=True)
    tiponombramiento = models.ForeignKey('SecretariaTiponombramiento', db_column='tipoNombramiento_id', blank=True, null=True) # Field name made lowercase.
    cargo_id = models.IntegerField()
    numerohoras = models.IntegerField(db_column='numeroHoras') # Field name made lowercase.
    estado_plaza = models.IntegerField()
    tipo_jornada = models.IntegerField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    observacion = models.IntegerField(blank=True, null=True)
    fuentepago = models.IntegerField(db_column='fuentePago') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'docente_plaza'

class DocenteTitulo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=8)
    descripcion = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'docente_titulo'

class DocenteTitulodocente(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.ForeignKey(DocenteTitulo)
    docente = models.ForeignKey(DocenteDocente)
    class Meta:
        managed = False
        db_table = 'docente_titulodocente'

class EstadisticaResumenapbRepb(models.Model):
    id = models.IntegerField(primary_key=True)
    centro_id = models.IntegerField()
    clase_id = models.IntegerField()
    nivel_id = models.IntegerField()
    apb = models.IntegerField()
    repb = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'estadistica_resumenapb_repb'

class EstadisticaResumenedades(models.Model):
    id = models.IntegerField(primary_key=True)
    centro_id = models.IntegerField()
    curso_id = models.IntegerField()
    edad = models.CharField(max_length=2)
    cantidad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'estadistica_resumenedades'

class EstadisticaResumenmaestro(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.SmallIntegerField()
    departamento = models.ForeignKey('SecretariaDepartamento')
    municipio = models.ForeignKey('SecretariaMunicipio')
    aldea = models.ForeignKey('SecretariaAldea')
    centro = models.ForeignKey('SecretariaCentroeducativo')
    nivel = models.ForeignKey('SecretariaNiveleducativo')
    sub_nivel = models.ForeignKey('SecretariaSubNiveleducativo')
    curso = models.ForeignKey('SecretariaCurso')
    parcial = models.SmallIntegerField()
    alumno = models.ForeignKey(AlumnosAlumno)
    clase = models.ForeignKey('SecretariaClase')
    nota = models.SmallIntegerField()
    edad = models.SmallIntegerField()
    genero = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'estadistica_resumenmaestro'

class EstadisticaResumennotas(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.IntegerField()
    departamento = models.ForeignKey('SecretariaDepartamento')
    municipio = models.ForeignKey('SecretariaMunicipio')
    clase = models.CharField(max_length=128)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    curso = models.ForeignKey('SecretariaCurso')
    class Meta:
        managed = False
        db_table = 'estadistica_resumennotas'

class ExamenesPregunta(models.Model):
    id = models.IntegerField(primary_key=True)
    clase_id = models.IntegerField()
    curso_id = models.IntegerField()
    pregunta = models.TextField()
    respuesta = models.TextField()
    ecuacion = models.CharField(max_length=512, blank=True)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    section = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'examenes_pregunta'

class ExamenesSection(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    multipregunta = models.BooleanField()
    multirespuesta = models.BooleanField()
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'examenes_section'

class InventarioInventario(models.Model):
    id = models.IntegerField(primary_key=True)
    producto = models.ForeignKey('InventarioProducto')
    cantidad = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'inventario_inventario'

class InventarioOperacionproducto(models.Model):
    id = models.IntegerField(primary_key=True)
    producto = models.ForeignKey('InventarioProducto')
    cantidad = models.IntegerField()
    accion = models.IntegerField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'inventario_operacionproducto'

class InventarioProducto(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'inventario_producto'

class MensajeriaMensaje(models.Model):
    id = models.IntegerField(primary_key=True)
    ventana = models.ForeignKey('MensajeriaVentana')
    emisor = models.ForeignKey(AuthUser)
    mensaje = models.CharField(max_length=600)
    fecha_hora = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mensajeria_mensaje'

class MensajeriaMensajeestado(models.Model):
    id = models.IntegerField(primary_key=True)
    mensaje = models.ForeignKey(MensajeriaMensaje)
    receptor = models.ForeignKey(AuthUser)
    leido = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'mensajeria_mensajeestado'

class MensajeriaUserventana(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    ventana = models.ForeignKey('MensajeriaVentana')
    class Meta:
        managed = False
        db_table = 'mensajeria_userventana'

class MensajeriaVentana(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_apertura = models.DateTimeField()
    tipo = models.IntegerField()
    activa = models.BooleanField()
    oculta = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'mensajeria_ventana'

class MenusCachekey(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=255)
    site = models.IntegerField()
    key = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'menus_cachekey'

class NotasNotaparcial(models.Model):
    id = models.IntegerField(primary_key=True)
    acumulativo = models.IntegerField(blank=True, null=True)
    examen = models.IntegerField(blank=True, null=True)
    matricula = models.ForeignKey(AlumnosMatricula)
    clase_seccion = models.ForeignKey(CentroeducativoClaseseccion)
    parcial = models.ForeignKey(CentroeducativoParcial, blank=True, null=True)
    equivalencia = models.BooleanField()
    nivelacion = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'notas_notaparcial'

class NotasNotarecuperacion(models.Model):
    id = models.IntegerField(primary_key=True)
    acumulativo = models.IntegerField(blank=True, null=True)
    examen = models.IntegerField(blank=True, null=True)
    matricula = models.ForeignKey(AlumnosMatricula)
    clase_seccion = models.ForeignKey(CentroeducativoClaseseccion)
    recuperacion = models.ForeignKey(CentroeducativoRecuperacion, blank=True, null=True)
    nivelacion = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'notas_notarecuperacion'

class NotasNotaretrasada(models.Model):
    id = models.IntegerField(primary_key=True)
    acumulativo = models.IntegerField(blank=True, null=True)
    examen = models.IntegerField(blank=True, null=True)
    parcial = models.ForeignKey(CentroeducativoParcial)
    nivelacion = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'notas_notaretrasada'

class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=65)
    pbc_tid = models.IntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=65)
    pbc_cnam = models.CharField(max_length=65)
    pbc_cid = models.SmallIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=254, blank=True)
    pbc_lpos = models.SmallIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True)
    pbc_hpos = models.SmallIntegerField(blank=True, null=True)
    pbc_jtfy = models.SmallIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=31, blank=True)
    pbc_case = models.SmallIntegerField(blank=True, null=True)
    pbc_hght = models.SmallIntegerField(blank=True, null=True)
    pbc_wdth = models.SmallIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=31, blank=True)
    pbc_bmap = models.CharField(max_length=1, blank=True)
    pbc_init = models.CharField(max_length=254, blank=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True)
    pbc_edit = models.CharField(max_length=31, blank=True)
    pbc_tag = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatcol'

class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30)
    pbe_edit = models.CharField(max_length=254, blank=True)
    pbe_type = models.SmallIntegerField(blank=True, null=True)
    pbe_cntr = models.IntegerField(blank=True, null=True)
    pbe_seqn = models.SmallIntegerField()
    pbe_flag = models.IntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatedt'

class Pbcatfmt(models.Model):
    pbf_name = models.CharField(unique=True, max_length=30)
    pbf_frmt = models.CharField(max_length=254, blank=True)
    pbf_type = models.SmallIntegerField(blank=True, null=True)
    pbf_cntr = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pbcatfmt'

class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=65)
    pbt_tid = models.IntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=65)
    pbd_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True)
    pbd_funl = models.CharField(max_length=1, blank=True)
    pbd_fchr = models.SmallIntegerField(blank=True, null=True)
    pbd_fptc = models.SmallIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=18, blank=True)
    pbh_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True)
    pbh_funl = models.CharField(max_length=1, blank=True)
    pbh_fchr = models.SmallIntegerField(blank=True, null=True)
    pbh_fptc = models.SmallIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=18, blank=True)
    pbl_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True)
    pbl_funl = models.CharField(max_length=1, blank=True)
    pbl_fchr = models.SmallIntegerField(blank=True, null=True)
    pbl_fptc = models.SmallIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=18, blank=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcattbl'

class Pbcatvld(models.Model):
    pbv_name = models.CharField(unique=True, max_length=30)
    pbv_vald = models.CharField(max_length=254, blank=True)
    pbv_type = models.SmallIntegerField(blank=True, null=True)
    pbv_cntr = models.IntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatvld'

class PmatriculaPrealumno(models.Model):
    id = models.IntegerField(primary_key=True)
    encargado = models.ForeignKey('PmatriculaPrepadrefamilia', blank=True, null=True)
    persona = models.ForeignKey('PmatriculaPrepersona', unique=True)
    class Meta:
        managed = False
        db_table = 'pmatricula_prealumno'

class PmatriculaPredocente(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey('PmatriculaPrepersona', unique=True)
    class Meta:
        managed = False
        db_table = 'pmatricula_predocente'

class PmatriculaPrematricula(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    ordenamiento = models.ForeignKey('SecretariaOrdenamientogrado', blank=True, null=True)
    alumno = models.ForeignKey(PmatriculaPrealumno)
    class Meta:
        managed = False
        db_table = 'pmatricula_prematricula'

class PmatriculaPrepadrefamilia(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey('PmatriculaPrepersona', unique=True)
    class Meta:
        managed = False
        db_table = 'pmatricula_prepadrefamilia'

class PmatriculaPrepersona(models.Model):
    id = models.IntegerField(primary_key=True)
    identidad = models.CharField(unique=True, max_length=13)
    primer_nombre = models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60, blank=True)
    primer_apellido = models.CharField(max_length=60)
    segundo_apellido = models.CharField(max_length=60, blank=True)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateTimeField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9, blank=True)
    lugar_nacimiento = models.CharField(max_length=150, blank=True)
    correo = models.CharField(max_length=75)
    class Meta:
        managed = False
        db_table = 'pmatricula_prepersona'

class PrafPersonaPerpersona(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(CuentasPersona, unique=True)
    per_persona = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = 'praf_persona_perpersona'

class PrafResumenPraf(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    periodo = models.DateField()
    cantidad = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'praf_resumen_praf'

class SecretariaAldea(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=128)
    municipio = models.ForeignKey('SecretariaMunicipio')
    class Meta:
        managed = False
        db_table = 'secretaria_aldea'

class SecretariaAreasPreguntas(models.Model):
    id = models.IntegerField(primary_key=True)
    area_inversion = models.ForeignKey('SecretariaAreasReparacion')
    centro_pregunta = models.ForeignKey('SecretariaCentroPreguntas')
    class Meta:
        managed = False
        db_table = 'secretaria_areas_preguntas'

class SecretariaAreasReparacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=32)
    class Meta:
        managed = False
        db_table = 'secretaria_areas_reparacion'

class SecretariaBarrio(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=128)
    caserio = models.ForeignKey('SecretariaCaserio')
    class Meta:
        managed = False
        db_table = 'secretaria_barrio'

class SecretariaBeneficalprograms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'secretaria_beneficalprograms'

class SecretariaCaserio(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=128)
    aldea = models.ForeignKey(SecretariaAldea)
    class Meta:
        managed = False
        db_table = 'secretaria_caserio'

class SecretariaCentroCodigoapp(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    codigoapp = models.ForeignKey('SecretariaCodigoapp')
    class Meta:
        managed = False
        db_table = 'secretaria_centro_codigoapp'

class SecretariaCentroJornada(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    jornada = models.ForeignKey('SecretariaJornada')
    class Meta:
        managed = False
        db_table = 'secretaria_centro_jornada'

class SecretariaCentroModalidad(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    modalidad = models.ForeignKey('SecretariaModalidad')
    class Meta:
        managed = False
        db_table = 'secretaria_centro_modalidad'

class SecretariaCentroOrganismo(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    organismo = models.ForeignKey('SecretariaOrganismo')
    fortalecido = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'secretaria_centro_organismo'

class SecretariaCentroPreguntas(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    hubo_inversion = models.IntegerField()
    monto_inversion = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'secretaria_centro_preguntas'

class SecretariaCentroSubNiveleducativo(models.Model):
    id = models.IntegerField(primary_key=True)
    centro = models.ForeignKey('SecretariaCentroeducativo')
    sub_niveleducativo = models.ForeignKey('SecretariaSubNiveleducativo')
    class Meta:
        managed = False
        db_table = 'secretaria_centro_sub_niveleducativo'

class SecretariaCentroeducativo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=14)
    nombre = models.CharField(max_length=256)
    abreviatura = models.CharField(max_length=16)
    departamento = models.ForeignKey('SecretariaDepartamento')
    municipio = models.ForeignKey('SecretariaMunicipio')
    aldea = models.ForeignKey(SecretariaAldea, blank=True, null=True)
    caserio = models.ForeignKey(SecretariaCaserio, blank=True, null=True)
    barrio = models.ForeignKey(SecretariaBarrio, blank=True, null=True)
    direccion_completa = models.CharField(max_length=256)
    en_funcionamiento = models.IntegerField()
    en_funcionamiento_anio = models.IntegerField()
    nofuncionamiento_motivo = models.CharField(max_length=128, blank=True)
    cambio_nombre = models.IntegerField()
    cambio_nombre_nombreanterior = models.CharField(max_length=256, blank=True)
    cambio_nombre_fechacambio = models.DateField(blank=True, null=True)
    cambio_nombre_acuerdo = models.CharField(max_length=32, blank=True)
    tipo_administracion = models.ForeignKey('SecretariaTipoadministracion')
    tipo_zona = models.ForeignKey('SecretariaTipozona')
    periodo_escolar = models.ForeignKey('SecretariaPeriodoescolar')
    fronterizo = models.IntegerField()
    pais_fronterizo = models.ForeignKey('SecretariaPais', blank=True, null=True)
    distancia_km = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo_docente = models.ForeignKey('SecretariaTipoDocente', unique=True, blank=True, null=True)
    pueblo_etnico = models.ForeignKey('SecretariaPuebloEtnico', blank=True, null=True)
    tel_fijo = models.CharField(max_length=8, blank=True)
    tel_celular = models.CharField(max_length=8, blank=True)
    correo = models.CharField(max_length=128, blank=True)
    codigo_estadistico = models.CharField(max_length=10, blank=True)
    bloqueado = models.BooleanField()
    usuario_creador = models.ForeignKey(AuthUser, blank=True, null=True)
    usuario_modifico = models.ForeignKey(AuthUser, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    electricity = models.IntegerField()
    comunity_electricity = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'secretaria_centroeducativo'

class SecretariaClase(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=128)
    descripcion = models.CharField(max_length=256)
    multihorario = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'secretaria_clase'

class SecretariaClasesMallacurricularoficial(models.Model):
    id = models.IntegerField(primary_key=True)
    clase = models.ForeignKey(SecretariaClase)
    mallacurricularoficial = models.ForeignKey('SecretariaMallacurricularoficial', db_column='MallaCurricularOficial_id') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'secretaria_clases_mallacurricularoficial'

class SecretariaCodigoapp(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'secretaria_codigoapp'

class SecretariaCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    horas_clases = models.IntegerField()
    sub_nivel_educativo = models.ForeignKey('SecretariaSubNiveleducativo')
    ordenamiento = models.ForeignKey('SecretariaOrdenamientogrado')
    modalidad = models.ForeignKey('SecretariaModalidad')
    requisito = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'secretaria_curso'

class SecretariaDepartamento(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=2)
    nombre = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'secretaria_departamento'

class SecretariaEib(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'secretaria_eib'

class SecretariaEibInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    institution = models.ForeignKey(SecretariaCentroeducativo)
    eib = models.ForeignKey(SecretariaEib)
    class Meta:
        managed = False
        db_table = 'secretaria_eib_institution'

class SecretariaElectricalprecedence(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    class Meta:
        managed = False
        db_table = 'secretaria_electricalprecedence'

class SecretariaElectricalprecedenceInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    precedence = models.ForeignKey(SecretariaElectricalprecedence)
    institution = models.ForeignKey(SecretariaCentroeducativo)
    class Meta:
        managed = False
        db_table = 'secretaria_electricalprecedence_institution'

class SecretariaJornada(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=32)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    class Meta:
        managed = False
        db_table = 'secretaria_jornada'

class SecretariaMallacurricularoficial(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    curso = models.ForeignKey(SecretariaCurso)
    activa = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'secretaria_mallacurricularoficial'

class SecretariaModalidad(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    descripcion = models.CharField(unique=True, max_length=128)
    abreviatura = models.CharField(unique=True, max_length=32, blank=True)
    min_ordenamiento = models.ForeignKey('SecretariaOrdenamientogrado', blank=True, null=True)
    max_ordenamiento = models.ForeignKey('SecretariaOrdenamientogrado', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'secretaria_modalidad'

class SecretariaMunicipio(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=128)
    departamento = models.ForeignKey(SecretariaDepartamento)
    class Meta:
        managed = False
        db_table = 'secretaria_municipio'

class SecretariaNivelacademico(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'secretaria_nivelacademico'

class SecretariaNiveleducativo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(unique=True, max_length=64)
    requisito = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'secretaria_niveleducativo'

class SecretariaOrdenamientogrado(models.Model):
    id = models.IntegerField(primary_key=True)
    ordenamiento = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=64)
    valor = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'secretaria_ordenamientogrado'

class SecretariaOrganismo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'secretaria_organismo'

class SecretariaOrganization(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'secretaria_organization'

class SecretariaOrganizationInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    institution = models.ForeignKey(SecretariaCentroeducativo)
    organization = models.ForeignKey(SecretariaOrganization)
    class Meta:
        managed = False
        db_table = 'secretaria_organization_institution'

class SecretariaPais(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(unique=True, max_length=128)
    gentilicio = models.CharField(max_length=128)
    abreviatura = models.CharField(max_length=32)
    class Meta:
        managed = False
        db_table = 'secretaria_pais'

class SecretariaPeriodoescolar(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=64)
    mesinicio = models.IntegerField(db_column='mesInicio', blank=True, null=True) # Field name made lowercase.
    mesfinaliza = models.IntegerField(db_column='mesFinaliza', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'secretaria_periodoescolar'

class SecretariaPermisocentro(models.Model):
    id = models.IntegerField(primary_key=True)
    permiso = models.ForeignKey(AuthPermission, unique=True)
    descripcion = models.CharField(max_length=128)
    centro_app = models.ForeignKey(SecretariaCodigoapp, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'secretaria_permisocentro'

class SecretariaProgramInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    program = models.ForeignKey(SecretariaBeneficalprograms)
    institution = models.ForeignKey(SecretariaCentroeducativo)
    class Meta:
        managed = False
        db_table = 'secretaria_program_institution'

class SecretariaPuebloEtnico(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'secretaria_pueblo_etnico'

class SecretariaSubNiveleducativo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=64)
    nivel_educativo = models.ForeignKey(SecretariaNiveleducativo)
    min_anio = models.ForeignKey(SecretariaOrdenamientogrado)
    max_anio = models.ForeignKey(SecretariaOrdenamientogrado)
    class Meta:
        managed = False
        db_table = 'secretaria_sub_niveleducativo'

class SecretariaTipoDocente(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'secretaria_tipo_docente'

class SecretariaTipoadministracion(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'secretaria_tipoadministracion'

class SecretariaTipodocumentoid(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=32)
    longitud = models.IntegerField()
    tipo_campo = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'secretaria_tipodocumentoid'

class SecretariaTiponombramiento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=32)
    class Meta:
        managed = False
        db_table = 'secretaria_tiponombramiento'

class SecretariaTipozona(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'secretaria_tipozona'

class SnippetSnippet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    html = models.TextField()
    template = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'snippet_snippet'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

class TaggingTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'tagging_tag'

class TaggingTaggeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.ForeignKey(TaggingTag)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tagging_taggeditem'

class UtilityArchivo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=128)
    archivo = models.CharField(max_length=100)
    activo = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'utility_archivo'

class ZinniaCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'zinnia_category'

class ZinniaEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField()
    tags = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    status = models.IntegerField()
    featured = models.BooleanField()
    comment_enabled = models.BooleanField()
    pingback_enabled = models.BooleanField()
    creation_date = models.DateTimeField()
    last_update = models.DateTimeField()
    start_publication = models.DateTimeField(blank=True, null=True)
    end_publication = models.DateTimeField(blank=True, null=True)
    login_required = models.BooleanField()
    password = models.CharField(max_length=50)
    template = models.CharField(max_length=250)
    content_placeholder = models.ForeignKey(CmsPlaceholder, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zinnia_entry'

class ZinniaEntryAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    entry = models.ForeignKey(ZinniaEntry)
    author = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'zinnia_entry_authors'

class ZinniaEntryCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    entry = models.ForeignKey(ZinniaEntry)
    category = models.ForeignKey(ZinniaCategory)
    class Meta:
        managed = False
        db_table = 'zinnia_entry_categories'

class ZinniaEntryRelated(models.Model):
    id = models.IntegerField(primary_key=True)
    from_entry = models.ForeignKey(ZinniaEntry)
    to_entry = models.ForeignKey(ZinniaEntry)
    class Meta:
        managed = False
        db_table = 'zinnia_entry_related'

class ZinniaEntrySites(models.Model):
    id = models.IntegerField(primary_key=True)
    entry = models.ForeignKey(ZinniaEntry)
    site = models.ForeignKey(DjangoSite)
    class Meta:
        managed = False
        db_table = 'zinnia_entry_sites'

