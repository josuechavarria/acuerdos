#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import permission_required, login_required
from acuerdos.general.forms import *
# Create your views here. please
from acuerdos.general.models_see import *
from acuerdos.acuerdo.models_sace import *

@login_required
def view_index(request):
	'''for depto in EeMunicipios.objects.using('siarhd').filter(departamento_id__descripcion_departamento='YORO'):
		print depto.descripcion_municipio'''
	return render_to_response('general/menu-principal.html', context_instance=RequestContext(request))

def view_login_1(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('vista_inicio')) #redirecciona a la raiz
	else:
		if request.method=="POST":
			form = FormLogin(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active: #si el usuario no es nullo y esta activo
					login(request, usuario) #crea la sesion
					return HttpResponseRedirect(reverse('vista_inicio')) #redirecciona a la raiz
				else:
					mensaje = "La combinación Usuario y Contraseña es incorrecta"	
		form = FormLogin()
		ctx={'formulario':form, 'mensaje':mensaje}			
		return render_to_response('general/login.html', ctx, context_instance=RequestContext(request))
def view_login(request):	
	mensaje=""

	if request.user.is_authenticated():	
		if request.user.groups.get().name == 'director':
			print request.user.first_name
			return HttpResponseRedirect(reverse('vista_inicio'))
		if request.user.is_superuser:
			return HttpResponseRedirect(reverse('vista_inicido'))
	else:
		if request.method == "POST":
			form = FormLogin(request.POST)
			if form.is_valid():
				u=form.cleaned_data['username']
				p=form.cleaned_data['password']
				usuario=authenticate(username=u, password=p)
				if usuario is not None:
					if usuario.is_active:
						print "logueado"
						login(request, usuario) #crea la sesion	
						return HttpResponseRedirect(reverse('vista_inicio'))						
					else:
						mensaje = "Su cuenta está inactiva"
				else:
					print "busca en sace"
					if AuthUser.objects.using("sace").filter(username=u):
						director=AuthUser.objects.using("sace").get(username=u)
						print "encontro username"
						if AuthUserGroups.objects.using("sace").filter(user=director.pk, group__pk=1):
							print "ES DIRECTOR"
							if len(User.objects.filter(username = director.username)) == 0:
								user = User.objects.create_user(username = director.username, password = director.password, email=director.email, first_name = director.first_name, last_name = director.last_name)						
								user.groups.add(Group.objects.get(name = 'director'))#grupo ESTUDIANTE
								user.password=director.password
								user.save()											
							else:
								#user = User.objects.get(username = director.username)
								print u
								print p
								us=authenticate(username=u, password=p)
								if us is not None and us.is_active==True: #si el usuario no es nullo y esta activo
									login(request, us) #crea la sesion
									return HttpResponseRedirect(reverse('vista_inicio')) #redirecciona a la raiz
								else:
									mensaje = "La combinación Usuario y Contraseña es incorrecta"
						
							#return HttpResponseRedirect(reverse('vista_inicio'))	
						else:
							print "NO ES DIRECTOR"										
					else:
						mensaje = "La combinación Usuario y Contraseña es incorrecta"

		form = FormLogin()
		ctx={'formulario':form, 'mensaje':mensaje}			
		return render_to_response('general/login.html', ctx, context_instance=RequestContext(request))


def view_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

