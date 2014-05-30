#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from acuerdos.general.models import *

# Create your models here.

class plazas(models.Model):
	cuenta=models.CharField(max_length=50)
	horas=models.IntegerField(null = True, blank = True,default = None)
	estado=models.IntegerField()
	descripcion_estado=models.CharField(max_length=50)
	institucion=models.IntegerField()
	programa=models.IntegerField()
	subprograma=models.IntegerField()
	fuente=models.IntegerField()
	codigo_departamento=models.CharField(max_length=4)
	codigo_muncipio=models.CharField(max_length=4)
	codigo_centro=models.CharField(max_length=6)
	numero_plaza=models.CharField(max_length=6)
	codigo_aldea=models.CharField(max_length=4)
	nivel_educativo=models.CharField(max_length=6)
	direccion_centro=models.CharField(max_length=512, null = True, blank = True,default = None)
	nombre_centro=models.CharField(max_length=255, verbose_name="Nombre del centro")
	cambio_estado=models.BooleanField(default=False)
	nuevo_estado=models.ForeignKey(estados_plaza, max_length=50, null = True, blank = True,default = None)
	usuario_modificador=models.ForeignKey(User, related_name='plaza_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return '(%s | %s | %s | %s) - %s' % (self.codigo_departamento,self.codigo_muncipio,self.codigo_centro,self.numero_plaza, self.nombre_centro)

	class Meta:
		verbose_name_plural = "plazas en el siarhd"

class plazas_disponibles(models.Model):
	Jornada_CHOICES = (('Matutina', 'Matutina'),('Vespertina', 'Vespertina'),('Matutina y Vespertina', 'Matutina y Vespertina'),('Extendida', 'Extendida'),('Nocturna', 'Nocturna'),('Matutina y Nocturna', 'Matutina y Nocturna'),('Vespertina y Nocturna', 'Vespertina y Nocturna'))
	codigo_centro=models.CharField(max_length=9, verbose_name="Código estadístico")
	nivel_educativo=models.ForeignKey(subniveles_educativos)
	cargo=models.ForeignKey(cargos, help_text="Seleccione el cargo por el cual está registrando la plaza.")
	jornada=models.ManyToManyField(jornadas, verbose_name="Jornada", help_text="Puede seleccionar mas de una opción.")
	motivo=models.ForeignKey(motivos)
	horas=models.IntegerField(verbose_name="Total de horas", help_text="Indique el total de horas por semana de la plaza.", max_length=3)
	disponible=models.BooleanField(default=True)
	observacion=models.TextField(verbose_name="Observación")
	visible=models.BooleanField(default=True, verbose_name="¿Disponible?")
	usuario_modificador=models.ForeignKey(User, related_name='plazadisponible_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	class Meta:
		permissions = (
			("can_view_plazas_disponibles", "Puede ver las plazas disponibles de su centro"),
		)
		verbose_name_plural = "plazas disponibles"

class acuerdo_basica(models.Model):
	#infomacion general del acuerdo
	plaza_disponible=models.ForeignKey(plazas_disponibles)
	accion=models.CharField(max_length=30, verbose_name="Acción No.")
	nacuerdo=models.CharField(max_length=20, verbose_name="Acuerdo #")
	fecha=models.DateField(default=datetime.now())
	movimiento=models.ForeignKey(subtipos_acuerdos)
	vigencia_desde=models.DateField()
	vigencia_hasta=models.DateField(default=None, null=True)
	#infomacion del docente
	clave_escalafon_docente=models.CharField(max_length=15, verbose_name="Clave de escalafon")
	nombres_docente=models.CharField(max_length=45, verbose_name="Nombres")
	apellidos_docente=models.CharField(max_length=45, verbose_name="Apellidos")
	identidad_docente=models.CharField(max_length=13, verbose_name="Identidad")
	sexo_docente=models.CharField(max_length=10)
	fecha_nacimiento_docente=models.DateField(verbose_name="Fecha Nacimiento")
	colegio1=models.ForeignKey(colegios_magisteriales, related_name="acuerdo_b_colegio1")
	colegio2=models.ForeignKey(colegios_magisteriales, related_name="acuerdo_b_colegio2", null=True, default=None, blank=True)
	numero_imprema=models.CharField(max_length=15, verbose_name="Número INPREMA")
	estado_docente=models.CharField(max_length=25, verbose_name="Nota de concurso")
	#informacion del centro educativo
	cargo=models.ForeignKey(cargos, verbose_name="Cargo a ocupar")
	codigo_centro=models.CharField(max_length=9, verbose_name="Código estadístico")
	nombre_centro=models.CharField(max_length=255, verbose_name="Escuela")
	departamento=models.ForeignKey(departamento)
	municipio=models.ForeignKey(municipio)
	aldea=models.ForeignKey(aldea)
	#informacion de la plaza
	estructura_plaza=models.CharField(max_length=20)
	estructura_presupuestaria=models.CharField(max_length=15)
	jornada_laboral=models.ForeignKey(jornadas_laborales, verbose_name="JORNADA LABORAL")
	justificacion=models.TextField()
	estado=models.ForeignKey(estados_acuerdo)
	usuario_creador=models.ForeignKey(User, related_name='acuerdo_basica_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='acuerdo_basica_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	class Meta:
		permissions = (
			("can_view_acuerdos", "Puede entrar a admon de acuerdos"),
			("can_view_acuerdos_basica", "Puede entrar a admon de acuerdos basica"),
			("can_view_acuerdos_media", "Puede entrar a admon de acuerdos media"),
		)
		verbose_name_plural = "Acuerdos de basica"