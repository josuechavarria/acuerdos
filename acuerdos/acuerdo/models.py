#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from acuerdos.general.models import estados_plaza,cargos,motivos, niveles_educativos, subniveles_educativos, jornadas, tipos_movimientos

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
		return '(%s | %s | %s | %s) - %s' % (self.codigo_departamento,self.codigo_municipio,self.codigo_centro,self.numero_plaza, self.nombre_centro)

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

class acuerdo(models.Model):
	#infomacion general del acuerdo
	accion=models.CharField(max_length=30)
	fecha=models.DateField(default=datetime.now())
	movimiento=models.ForeignKey(tipos_movimientos)
	vigencia_desde=models.DateField()
	vigencia_hasta=models.DateField(default=None, null=True)
	#infomacion del docente
	clave_escalafon_docente=models.CharField(max_length=15)
	nombres_docente=models.CharField(max_length=45)
	apellidos_docente=models.CharField(max_length=45)
	identidad_docente=models.CharField(max_length=13)
	sexo_docente=models.CharField(max_length=10)
	fecha_nacimiento_docente=models.DateField()
	
	estado_docente=models.CharField(max_length=25)
	#informacion del centro educativo
	codigo_centro=models.CharField(max_length=9, verbose_name="Código estadístico")
	nombre_centro=models.CharField(max_length=255, verbose_name="Nombre Centro")


	