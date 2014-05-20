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

@login_required
def view_plazas_inicio(request):
	if AuthUser.objects.using("sace").filter(username=request.user.username):
		user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
		if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
			centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
	print centro.centro
	ctx = {'centro': centro.centro.nombre}
	return render_to_response('acuerdo/inicio-plazas.html', ctx, context_instance=RequestContext(request))

@login_required
def view_acuerdos_inicio(request):
	user=User.objects.get(pk=request.user.pk)
	ctx = {'departamento': user.departamento.descripcion}
	return render_to_response('acuerdo/inicio-acuerdos.html', ctx, context_instance=RequestContext(request))


@permission_required('acuerdo.add_plazas_disponibles', login_url='/inicio/')
def view_plazas_nuevo(request):
	#recuperar datos del centro
		user_id=[]
		centro=[]
		if AuthUser.objects.using("sace").filter(username=request.user.username):
			user_id=AuthUser.objects.using("sace").get(username=request.user.username).pk
			if CuentasUserCentroJornada.objects.using("sace").filter(usuario_id=user_id):
				centro= CuentasUserCentroJornada.objects.using("sace").get(usuario_id=user_id)
		subnivel=list(SecretariaCentroSubNiveleducativo.objects.using("sace").filter(centro=centro.centro.pk).values_list('sub_niveleducativo', flat=True))
		jornada=list(SecretariaCentroJornada.objects.using("sace").filter(centro=centro.centro.pk).values_list('jornada', flat=True))
		if request.method == 'POST':
			print "salvando1"
			formulario = PlazasForm(subnivel, jornada, request.POST)		
			if formulario.is_valid():
				print "salvando"
				form = formulario.save(commit = False)
				form.visible=True
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				formulario.save_m2m()
				#retornar exito
				formulario = PlazasForm(subnivel, jornada)
				ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'exito':"si"}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request))
			else:
				ctx = {'formulario':formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'error':'cx'}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = PlazasForm(subnivel, jornada)
			ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre}
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
		subnivel=list(SecretariaCentroSubNiveleducativo.objects.using("sace").filter(centro=centro.centro.pk).values_list('sub_niveleducativo', flat=True))
		jornada=list(SecretariaCentroJornada.objects.using("sace").filter(centro=centro.centro.pk).values_list('jornada', flat=True))

		#Recuperar objeto plazas
		plaza=plazas_disponibles.objects.get(pk=plaza_id)
		print plaza.jornada.all()
		if request.method == 'POST':
			print "datos por post"
			formulario = PlazasForm(subnivel, jornada, request.POST, instance=plaza)		
			if formulario.is_valid():
				print "salvando"
				form = formulario.save(commit = False)
				form.visible=True
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				formulario.save_m2m()
				#retornar exito
				formulario = PlazasForm(subnivel, jornada, instance=plaza)
				ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'nivel':plaza.nivel_educativo.pk, 'jornadas_centro':plaza.jornada.all(), 'exito':"si"}
				return render_to_response('acuerdo/plazas-disponibles-editar.html', ctx, context_instance=RequestContext(request))
			else:
				ctx = {'formulario':formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'subnivel':subnivel, 'jornada':jornada, 'nivel':plaza.nivel_educativo.pk, 'jornadas_centro':plaza.jornada.all(), 'error':'cx'}
				return render_to_response('acuerdo/plazas-disponibles-editar.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = PlazasForm(subnivel, jornada, instance=plaza)
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
	ctx = {'plazas': plazas, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre}
	return render_to_response('acuerdo/centro-listado-plazas.html', ctx, context_instance=RequestContext(request))

@permission_required('acuerdo.can_view_plazas_disponibles', login_url='/inicio/')
def view_dd_plazas_listar(request):
	user=User.objects.get(pk=request.user.pk)
	plazas=plazas_disponibles.objects.filter(codigo_centro__startswith=user.departamento.codigo_departamento, visible=True, disponible=True)
	plazas_centros=[]
	for p in plazas:
		centro=SecretariaCentroeducativo.objects.using("sace").get(codigo__startswith=p.codigo_centro)
		director=CuentasPersona.objects.using("sace").get(identidad=p.usuario_modificador.username[:13])
		plazas_centros.append({
			'pk': p.pk,
			'municipio': centro.municipio.nombre,
			'aldea': centro.aldea.nombre,
			'codigo_centro': p.codigo_centro,
			'nombre_centro': centro.nombre,
			'direccion_centro': centro.direccion_completa,
			'nivel_educativo': p.nivel_educativo,
			'cargo': p.cargo,
			'jornada': p.jornada,
			'motivo': p.motivo,
			'horas': p.horas,
			'observacion': p.observacion,
			'nombre_director': director.primer_nombre+' '+director.segundo_nombre+' '+director.primer_apellido+' '+director.segundo_apellido,
			'telefono_director': director.telefono,
			'correo_director': director.correo
		})
	print plazas_centros
	ctx = {'plazas': plazas_centros}
	return render_to_response('acuerdo/dd-listado-plazas.html', ctx, context_instance=RequestContext(request))


@permission_required('acuerdo.add_acuerdo_basica', login_url='/inicio/')
def view_acuerdo_basica_nuevo(request, plaza_id):
	#recuperar datos del centro
		if request.method == 'POST':
			print "salvando1"
			formulario = PlazasForm(subnivel, jornada, request.POST)		
			if formulario.is_valid():
				print "salvando"
				form = formulario.save(commit = False)
				form.visible=True
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				formulario.save_m2m()
				#retornar exito
				formulario = PlazasForm(subnivel, jornada)
				ctx = {'formulario': formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'exito':"si"}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request))
			else:
				ctx = {'formulario':formulario, 'codigo_centro': centro.centro.codigo[:9], 'nombre_centro': centro.centro.nombre, 'error':'cx'}
				return render_to_response('acuerdo/plazas-disponibles-nuevo.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = AcuerdoBasicaForm()
			ctx = {'formulario': formulario}
			return render_to_response('acuerdo/acuerdo-basica-nuevo.html', ctx, context_instance=RequestContext(request))