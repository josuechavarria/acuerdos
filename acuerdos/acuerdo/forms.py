#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms
from django.forms import ModelForm, formsets, fields
from acuerdos.acuerdo.models import *
from acuerdos.general.models import *
from acuerdos.acuerdo.models_sace import *

class PlazasForm(ModelForm):
	class Meta:
		model = plazas_disponibles
		exclude = ('usuario_modificador', 'fecha_modificacion')
	disponible=forms.BooleanField(label=u'¿Disponible?', widget=forms.CheckboxInput(attrs={'class': 'ace ace-switch ace-switch-5', 'checked':'true'}))
	horas=forms.IntegerField(label=u'Horas', widget=forms.TextInput(attrs={'class': 'input-mini'}))