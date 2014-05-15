#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser

# Create your models here.

class  departamento(models.Model):
	codigo_departamento=models.CharField(max_length=4)
	descripcion=models.CharField(max_length=64, verbose_name="descripción")

	def __unicode__(self):
		return '%s | %s' % (self.codigo_departamento,self.descripcion)

	
class municipio(models.Model):
	codigo_municipio=models.CharField(max_length=4)
	departamento=models.ForeignKey(departamento)
	descripcion=models.CharField(max_length=64, verbose_name="descripción")

	def __unicode__(self):
		return '%s | %s' % (self.codigo_municipio,self.descripcion)


class aldea(models.Model):
	codigo_departamento=models.CharField(max_length=4)
	codigo_municipio=models.CharField(max_length=4)
	codigo_aldea=models.CharField(max_length=4)
	descripcion=models.CharField(max_length=255, verbose_name="descripción")
	municipio=models.ForeignKey(municipio)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		unique_together = ('codigo_departamento','codigo_municipio', 'codigo_aldea')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo_departamento','codigo_municipio', 'codigo_aldea'):
			return 'Ya existe esta aldea para el municipio y departamento especificado.'
		else:
			return super(aldea, self).unique_error_message(model_class, unique_check)

class centros(models.Model):
	codigo_departamento=models.CharField(max_length=4)
	codigo_municipio=models.CharField(max_length=4)
	codigo_aldea=models.CharField(max_length=4)
	nivel_educativo=models.CharField(max_length=6)
	direccion=models.CharField(max_length=512, null = True, blank = True,default = None)
	codigo=models.CharField(max_length=6)
	nombre=models.CharField(max_length=255, verbose_name="Nombre")

	def __unicode__(self):
		return '(%s | %s | %s) - %s' % (self.codigo_departamento,self.codigo_municipio,self.codigo,self.nombre)

	class Meta:
		unique_together = ('codigo_departamento','codigo_municipio', 'codigo')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo_departamento','codigo_municipio', 'codigo'):
			return 'Ya existe el centro educativo en esta ubicación.'
		else:
			return super(centros, self).unique_error_message(model_class, unique_check)

class estados_plaza(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "estados de la plaza"

class motivos(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "motivos"

class tipos_acuerdos(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "tipos de acuerdos"

class subtipos_acuerdos(models.Model):
	tipo_acuerdo=models.ForeignKey(tipos_acuerdos)
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return '%s | %s' % (self.tipo_acuerdo.descripcion,self.descripcion)

	class Meta:
		verbose_name_plural = "subtipos de acuerdos"

class cargos(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "cargos"

class jornadas(models.Model):
	descripcion = models.CharField(unique=True, max_length=32)
	hora_inicio = models.TimeField()
	hora_final = models.TimeField()

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "tipos de jornadas"

class jornadas_laborales(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "jornadas laborales"

class niveles_educativos(models.Model):
	codigo = models.IntegerField(unique=True)
	nombre = models.CharField(unique=True, max_length=64)
	requisito = models.CharField(max_length=15, blank=True, null=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "niveles educativos"

class subniveles_educativos(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=64)
	nivel_educativo = models.ForeignKey(niveles_educativos)
	min_anio = models.IntegerField()
	max_anio = models.IntegerField()

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "subniveles educativos"

class modalidades(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "modalidades"

class asignaturas(models.Model):
	modalidad=models.ForeignKey(modalidades)
	descripcion_modalidad=models.CharField(max_length=255, verbose_name="modalidad")
	clase_id=models.IntegerField()
	asignatura=models.CharField(max_length=255, verbose_name="asignaturas")

	def __unicode__(self):
		return '%s | %s' % (self.descripcion_modalidad, self.asignatura)

	class Meta:
		verbose_name_plural = "asignaturas por carrera"

class curso(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")
	abreviatura=models.CharField(max_length=30, verbose_name='abreviatura')

	def __unicode__(self):
		return '%s (%s)' % (self.descripcion, self.abreviatura)

	class Meta:
		verbose_name_plural = "cursos"

class User(User):
	departamento = models.ForeignKey(departamento, verbose_name="Departamento donde labora")
	telefono = models.CharField(max_length = 10, null = True, blank = True,default = None)
	
	objects = UserManager()

	class Meta:
		verbose_name_plural = "Usuarios"