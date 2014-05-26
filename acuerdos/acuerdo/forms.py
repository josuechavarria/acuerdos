#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms
from django.forms import ModelForm, formsets, fields
from django.contrib.auth.models import User
from acuerdos.acuerdo.models import *
from acuerdos.general.models import *
from acuerdos.acuerdo.models_sace import *

class PlazasForm(ModelForm):
	class Meta:
		model = plazas_disponibles
		exclude = ('usuario_modificador', 'fecha_modificacion')
	nivel_educativo = forms.ModelChoiceField(queryset=niveles_educativos.objects.all())
	jornada = forms.ModelMultipleChoiceField(queryset = jornadas.objects.all(),widget=forms.SelectMultiple(attrs={'class':'width-40  chosen-select', 'data-placeholder':'Elija una jornada...'}))
	disponible=forms.BooleanField(label=u'¿Disponible?', widget=forms.CheckboxInput(attrs={'class': 'ace ace-switch ace-switch-5', 'checked':'true'}))
	horas=forms.IntegerField(label=u'Horas', widget=forms.TextInput(attrs={'class': 'input-mini'}))

	def __init__(self, subnivel, jornada, *args, **kwargs):
		super(PlazasForm, self).__init__(*args, **kwargs)

		if subnivel:
			self.fields['nivel_educativo'].queryset = subniveles_educativos.objects.filter(pk__in=subnivel)
		if jornada:
			self.fields['jornada'].queryset = jornadas.objects.filter(pk__in=jornada)

class AcuerdoBasicaForm(ModelForm):
	class Meta:
		model = acuerdo_basica
		exclude = ('plaza_disponible','usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	accion = forms.CharField(label="Acción #",widget=forms.TextInput(attrs={'size': '10', 'required':'required', 'pattern': '[0-9]{4,4}', 'title':'El número de acción debe tener 4 dígitos.'}))
	fecha = forms.CharField(label="Fecha parámetro",widget=forms.TextInput(attrs={'required':'required', 'class':'form-control date-picker', 'data-date-format':'dd/mm/yyyy'}))
	vigencia_desde = forms.DateField(label="Vigencia desde el",widget=forms.DateInput(attrs={'required':'required', 'class':'form-control date-picker', 'data-date-format':'dd/mm/yyyy'}))
	vigencia_hasta = forms.DateField(label="Hasta",widget=forms.DateInput(attrs={'required':'required', 'class':'form-control date-picker', 'data-date-format':'dd/mm/yyyy'}))
	nombres_docente = forms.CharField(label="Nombres",widget=forms.TextInput(attrs={'size': '30', 'readonly':'readonly', 'required':'required', 'pattern': '[a-zA-Z]{3,45}', 'title':'El nombre del docente no es permitido.'}))
	apellidos_docente = forms.CharField(label="Apellidos",widget=forms.TextInput(attrs={'size': '30', 'readonly':'readonly', 'required':'required', 'pattern': '[a-zA-Z]{3,45}', 'title':'El nombre del docente no es permitido.'}))
	identidad_docente = forms.CharField(label="Identidad",widget=forms.TextInput(attrs={'class':'form-control', 'size': '18', 'required':'required', 'pattern': '[0-9]{13,13}', 'title':'El número de identidad debe ser numérico y de 13 dígitos.'}))
	fecha_nacimiento_docente = forms.CharField(label="Fecha Nacimiento",widget=forms.TextInput(attrs={'required':'required', 'readonly':'readonly', 'class':'form-control date-picker', 'data-date-format':'dd/mm/yyyy'}))
	departamento = forms.ModelChoiceField(queryset=departamento.objects.all())
	municipio = forms.ModelChoiceField(queryset=municipio.objects.all())
	aldea = forms.ModelChoiceField(queryset=aldea.objects.all())
	nombre_centro = forms.CharField(label="Escuela ",widget=forms.TextInput(attrs={'size': '55', 'required':'required', 'readonly': 'readonly'}))

	def __init__(self, codigo_departamento, codigo_municipio, codigo_aldea, *args, **kwargs):
		super(AcuerdoBasicaForm, self).__init__(*args, **kwargs)

		if codigo_departamento:
			self.fields['departamento'].queryset = departamento.objects.filter(codigo_departamento=codigo_departamento)
		if codigo_municipio and codigo_departamento:
			self.fields['municipio'].queryset = municipio.objects.filter(departamento__codigo_departamento=codigo_departamento, codigo_municipio=codigo_municipio)
		if codigo_aldea and codigo_municipio and codigo_departamento:
			self.fields['aldea'].queryset = aldea.objects.filter(codigo_departamento=codigo_departamento, codigo_municipio=codigo_municipio, codigo_aldea=codigo_aldea)