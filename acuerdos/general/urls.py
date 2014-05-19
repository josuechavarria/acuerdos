from django.conf.urls import patterns, url

urlpatterns=patterns('acuerdos.general.views', 
		url(r'^$', 'view_login', name='vista_principal'),
		url(r'^inicio/$', 'view_index', name='vista_inicio'),
		url(r'^inicio/usuarios-crear$', 'view_usuarios_nuevo', name='vista_usuarios_nuevo'),
		url(r'^inicio/usuarios-recuperar-clave$', 'view_usuarios_recuperar_password', name='vista_usuarios_recuperar_password'),
		url(r'^inicio/usuarios-deshabilitar$', 'view_usuarios_deshabilitar', name='vista_usuarios_deshabilitar'),
		url(r'^accounts/login/$', 'view_logout', name='vista_login'),
		url(r'^accounts/logout/$', 'view_logout', name='vista_logout'),
)