#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm, formsets, fields
from django.contrib.auth.models import User
from acuerdos.acuerdo.models import *
from acuerdos.general.models import *
from acuerdos.acuerdo.models_sace import *

class FormLogin(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Usuario', 'class': 'form-control'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'},render_value=False))


class FormNuevoUsuario(forms.Form):
	identidad = forms.CharField(widget=forms.TextInput(attrs={'size': '13', 'required':'required', 'pattern': '[0-9]{13,13}', 'title':'El número de identidad debe ser numérico y de 13 dígitos.'}))
	nombres = forms.CharField(widget=forms.TextInput(attrs={'size': '30','required':'required', 'pattern': '[a-zA-Z\s]{3,30}', 'title':'El tamaño del nombre debe ser entre 3 y 30 letras.'}))
	apellidos = forms.CharField(widget=forms.TextInput(attrs={'size': '30', 'required':'required', 'pattern': '[a-zA-Z\s]{3,30}', 'title':'El tamaño de los apellidos debe ser entre 3 y 30 letras.'}))
	departamento = forms.ModelChoiceField(queryset=departamento.objects.all(), label="Ubicación")
	telefono = forms.CharField(widget=forms.TextInput(attrs={'size': '8', 'required':'required', 'pattern': '[0-9]{8,8}', 'title':'El número de telefono debe ser numérico y de 8 dígitos.'}))

class FormRecuperarclave(forms.Form):
	identidad = forms.CharField(widget=forms.TextInput(attrs={'size': '13', 'required':'required', 'pattern': '[0-9]{13,13}', 'title':'El número de identidad debe ser numérico y de 13 dígitos.'}))
	departamento = forms.ModelChoiceField(queryset=departamento.objects.all(), label="Ubicación")
	telefono = forms.CharField(widget=forms.TextInput(attrs={'size': '8', 'required':'required', 'pattern': '[0-9]{8,8}', 'title':'El número de telefono debe ser numérico y de 8 dígitos.'}))