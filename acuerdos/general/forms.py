#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

class FormLogin(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Usuario', 'class': 'form-control'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'},render_value=False))