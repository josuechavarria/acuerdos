#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models

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
	descripcion=models.CharField(max_length=250, verbose_name="descripción")
	municipio=models.ForeignKey(municipio)

	def __unicode__(self):
		return self.descripcion

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

class jornadas_laborales(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "jornadas laborales"

class niveles_educativos(models.Model):
	descripcion=models.CharField(max_length=255, verbose_name="descripción")

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "niveles educativos"

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