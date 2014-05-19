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
