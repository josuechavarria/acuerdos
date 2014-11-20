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

	Departamento = request.user.groups.get().id
	ctx = {'Departamento' : Departamento}
	print ctx;
	return render_to_response('general/menu-principal.html',ctx,context_instance=RequestContext(request))
    
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
								user = User.objects.create_user(username = director.username, password = director.password, email=director.email, first_name = director.first_name, last_name = director.last_name, departamento = departamento.objects.get(pk=01), telefono = 99999999)						
								user.groups.add(Group.objects.get(name = 'director'))#grupo ESTUDIANTE
								user.password=director.password 
								#user.departamento = departamento.objects.get(pk=19)
								#user.telefono = 99999999
								user.save()	
								us=authenticate(username=u, password=p)
								if us is not None and us.is_active==True: #si el usuario no es nullo y esta activo
									login(request, us) #crea la sesion
									return HttpResponseRedirect(reverse('vista_inicio')) #redirecciona a la raiz
								else:
									mensaje = "La combinación Usuario y Contraseña es incorrecta"										
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


@permission_required('auth.add_user', login_url='/inicio/')
def view_usuarios_nuevo(request):
	#recuperar datos del centro
		if request.method == 'POST':
			print "hizo post"
			formulario = FormNuevoUsuario(request.POST)		
			if formulario.is_valid():
				print "form is_valid"
				#generar usuario aleatorio identidad + 4 numeros random
				random_usuario = User.objects.make_random_password(length=4, allowed_chars='0123456789')
				random_password = User.objects.make_random_password(length=8, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
				usuario=formulario.cleaned_data['identidad']+str(random_usuario)
				nombre_completo=formulario.cleaned_data['nombres']+" "+formulario.cleaned_data['apellidos']
				grupo = Group.objects.get(id=2)
				user = User.objects.create_user(
					username=usuario, 
					email='example@example.com', 
					password=random_password,
					first_name=formulario.cleaned_data['nombres'],
					last_name=formulario.cleaned_data['apellidos'],
					departamento=formulario.cleaned_data['departamento'],
					telefono=formulario.cleaned_data['telefono']
				)
				user.groups.add(grupo)
				user.save()
				#retornar exito
				formulario = FormNuevoUsuario()
				ctx = {'formulario': formulario, 'exito':"si", 'nombre': nombre_completo, 'usuario': usuario, 'password':random_password}
			else:
				ctx = {'formulario':formulario, 'error':'cx'}		
		else:
			formulario = FormNuevoUsuario()
			ctx = {'formulario': formulario}
		return render_to_response('general/usuario-nuevo.html', ctx, context_instance=RequestContext(request))

@permission_required('auth.change_user', login_url='/inicio/')
def view_usuarios_recuperar_password(request):
	#recuperar datos del centro
		if request.method == 'POST':
			print "hizo post"
			formulario = FormRecuperarclave(request.POST)		
			if formulario.is_valid():
				print "form is_valid"
				#generar password aleatorio identidad + 4 numeros random
				random_password = User.objects.make_random_password(length=8, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
				if User.objects.filter(username__startswith=formulario.cleaned_data['identidad'][:9], departamento=formulario.cleaned_data['departamento'], telefono=formulario.cleaned_data['telefono']):
					user=User.objects.get(username__startswith=formulario.cleaned_data['identidad'][:9], departamento=formulario.cleaned_data['departamento'], telefono=formulario.cleaned_data['telefono'])
					usuario=user.username
					nombre_completo=user.get_full_name()
					user.set_password(random_password)
					user.save()
					#retornar exito
					formulario = FormRecuperarclave()
					ctx = {'formulario': formulario, 'exito':"si", 'nombre': nombre_completo, 'usuario': usuario, 'password':random_password}
				else:
					#retornar error
					ctx = {'formulario': formulario, 'error':'cx'}
			else:
				ctx = {'formulario':formulario, 'error':'cx'}
		else:
			formulario = FormRecuperarclave()
			ctx = {'formulario': formulario}
		return render_to_response('general/usuario-clave-recuperar.html', ctx, context_instance=RequestContext(request))

@permission_required('auth.change_user', login_url='/inicio/')
def view_usuarios_deshabilitar(request):
	#recuperar datos del centro
		if request.method == 'POST':
			print "hizo post"
			formulario = FormRecuperarclave(request.POST)		
			if formulario.is_valid():
				print "form is_valid"
				if User.objects.filter(username__startswith=formulario.cleaned_data['identidad'][:9], departamento=formulario.cleaned_data['departamento'], telefono=formulario.cleaned_data['telefono']):
					user=User.objects.get(username__startswith=formulario.cleaned_data['identidad'][:9], departamento=formulario.cleaned_data['departamento'], telefono=formulario.cleaned_data['telefono'])
					nombre_completo=user.get_full_name()
					user.is_active=False
					user.save()
					#retornar exito
					formulario = FormRecuperarclave()
					ctx = {'formulario': formulario, 'exito':"si", 'nombre': nombre_completo}
				else:
					#retornar error
					ctx = {'formulario': formulario, 'error':'cx'}
			else:
				ctx = {'formulario':formulario, 'error':'cx'}
		else:
			formulario = FormRecuperarclave()
			ctx = {'formulario': formulario}
		return render_to_response('general/usuario-deshabilitar.html', ctx, context_instance=RequestContext(request))

#def libro_pdf(request):    
 #   print "Adentro"            
   # if: acuerdo= None

  #  general= tipos_acuerdos.objects.get(id = 1)     
   
    #movimiento= tipos_movimientos.objects.get(id=1)

    #print acuerdo.municipio.descripcion
    #print tacuerdo.tipos_acuerdos.descripcion  


   # departamento = SecretariaDepartamento.objects.get(id = acuerdo.departamento_id)
    #centro=SecretariaCentroeducativo.objects.using("sace").get(codigo__startswith=p.codigo_centro)        
   # html = render_to_string('acuerdo/acuerdo_pdf.html', {'pagesize':'A4','general':general}, context_instance=RequestContext(request))
    # return generar_pdf(html)
