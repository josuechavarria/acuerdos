#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import permission_required, login_required
from acuerdos.acuerdo.forms import *

from acuerdos.acuerdo.models_siarhd import *
from acuerdos.acuerdo.models_sace import *


def view_plazas_inicio(request):
	if AuthUser.objects.using("sace").filter(username=request.user.username):
		user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
		if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
			centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
	print centro.centro
	ctx = {'centro': centro.centro.nombre}
	return render_to_response('acuerdo/inicio-plazas.html', ctx, context_instance=RequestContext(request))


@permission_required('acuerdo.add_plazas_disponibles', login_url='/inicio/')
def view_plazas_nuevo(request):
	#recuperar datos del centro
		user_id=[]
		centro=[]
		if AuthUser.objects.using("sace").filter(username=request.user.username):
			user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
			if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
				centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
		subnivel=SecretariaCentroSubNiveleducativo.objects.using("sace").filter(centro=centro.centro.pk)
		jornada=SecretariaCentroJornada.objects.using("sace").filter(centro=centro.centro.pk)
		if request.method == 'POST':
			print "salvando1"
			formulario = PlazasForm(request.POST)		
			if formulario.is_valid():
				print "salvando"
				form = formulario.save(commit = False)
				form.visible=True
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				formulario.save_m2m()
				#retornar exito
				formulario = PlazasForm()
				ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'exito':"si"}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request))
			else:
				ctx = {'formulario':formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'error':'cx'}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = PlazasForm()
			ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada}
			return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request))


@permission_required('acuerdo.change_plazas_disponibles', login_url='/inicio/')
def view_plazas_editar(request, plaza_id=None):
	#recuperar datos del centro
		user_id=[]
		centro=[]
		if AuthUser.objects.using("sace").filter(username=request.user.username):
			user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
			if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
				centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
		subnivel=SecretariaCentroSubNiveleducativo.objects.using("sace").filter(centro=centro.centro.pk)
		jornada=SecretariaCentroJornada.objects.using("sace").filter(centro=centro.centro.pk)

		#Recuperar objeto plazas
		plaza=plazas_disponibles.objects.get(pk=plaza_id)
		print plaza.jornada.all()
		if request.method == 'POST':
			print "datos por post"
			formulario = PlazasForm(request.POST, instance=plaza)		
			if formulario.is_valid():
				print "salvando"
				form = formulario.save(commit = False)
				form.visible=True
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				formulario.save_m2m()
				#retornar exito
				formulario = PlazasForm(instance=plaza)
				ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'nivel':plaza.nivel_educativo.pk, 'jornadas_centro':plaza.jornada.all(), 'exito':"si"}
				return render_to_response('acuerdo/plazas-disponibles-editar.html', ctx, context_instance=RequestContext(request))
			else:
				ctx = {'formulario':formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'nivel':plaza.nivel_educativo.pk, 'jornadas_centro':plaza.jornada.all(), 'error':'cx'}
				return render_to_response('acuerdo/plazas-disponibles-editar.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = PlazasForm(instance=plaza)
			ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'nivel':plaza.nivel_educativo.pk, 'jornadas_centro':plaza.jornada.all(),}
			return render_to_response('acuerdo/plazas-disponibles-editar.html', ctx, context_instance=RequestContext(request))


@permission_required('acuerdo.delete_plazas_disponibles', login_url='/inicio/menu-plazas/listar-plazas')
def view_plazas_eliminar(request,plaza_id=None):
	if plaza_id:
		plazas_disponibles.objects.filter(pk=plaza_id).delete()
		return HttpResponseRedirect(reverse('vista_plazas_listar'))


@permission_required('acuerdo.can_view_plazas_disponibles', login_url='/inicio/')
def view_plazas_listar(request):
	if AuthUser.objects.using("sace").filter(username=request.user.username):
		user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
		if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
			centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
	plazas=plazas_disponibles.objects.filter(codigo_centro=centro.centro.codigo[:9], visible=True, disponible=True)
	for p in plazas:
		print p.jornada.all()
	ctx = {'plazas': plazas, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre}
	return render_to_response('acuerdo/centro-listado-plazas.html', ctx, context_instance=RequestContext(request))