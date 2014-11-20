from django.conf.urls import patterns, url

urlpatterns=patterns('acuerdos.acuerdo.views', 
		url(r'^inicio/menu-plazas$', 'view_plazas_inicio', name='vista_plazas_inicio'),
		url(r'^inicio/menu-acuerdos$', 'view_acuerdos_inicio', name='vista_acuerdos_inicio'),
		url(r'^inicio/menu-plazas/nueva-plaza$', 'view_plazas_nuevo', name='vista_plazas_nuevo'),
		url(r'^inicio/menu-plazas/cambiar-plaza/(?P<plaza_id>\d+)/$', 'view_plazas_editar', name='vista_plazas_editar'),
		url(r'^inicio/menu-plazas/eliminar-plaza/(?P<plaza_id>\d+)/$', 'view_plazas_eliminar', name='vista_plazas_eliminar'),
		url(r'^inicio/menu-plazas/listar-plazas$', 'view_plazas_listar', name='vista_plazas_listar'),
		url(r'^inicio/menu-acuerdos/listar-plazas$', 'view_dd_plazas_listar', name='vista_dd_plazas_listar'),
		url(r'^inicio/menu-acuerdos/listar-acuerdos$', 'view_acuerdos_listar', name='vista_acuerdos_listar'),
		url(r'^inicio/menu-acuerdos/nuevo-acuerdo-basica/(?P<plaza_id>\d+)/$', 'view_acuerdo_basica_nuevo', name='vista_acuerdo_basica_nuevo'),
		url(r'^inicio/menu-acuerdos/nuevo-acuerdo-prebasica/(?P<plaza_id>\d+)/$', 'view_acuerdo_prebasica_nuevo', name='vista_acuerdo_prebasica_nuevo'),
		url(r'^inicio/menu-acuerdos/nuevo-acuerdo-media/(?P<plaza_id>\d+)/$', 'view_acuerdo_media_nuevo', name='vista_acuerdo_media_nuevo'),
		url(r'^inicio/menu-acuerdos/recuperar-docente/$', 'view_recuperar_docente', name='vista_recuperar_docente'),
		url(r'^inicio/menu-acuerdos/recuperar-estructura/$', 'view_recuperar_estructura', name='vista_recuperar_estructura'),
		#url(r'^inicio/menu-acuerdos/nuevo-acuerdo-basica/(?P<id>\d+)/$', 'libro_pdf', name='Vista_Libro_pdf'),
		url(r'^inicio/menu-acuerdos/nuevo-acuerdo-basica/$','libro_pdf', name='Vista_Libro_pdf'),

)

