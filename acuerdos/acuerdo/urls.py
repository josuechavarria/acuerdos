from django.conf.urls import patterns, url

urlpatterns=patterns('acuerdos.acuerdo.views', 
		url(r'^inicio/menu-plazas$', 'view_plazas_inicio', name='vista_plazas_inicio'),
		url(r'^inicio/menu-plazas/nueva-plaza$', 'view_plazas_nuevo', name='vista_plazas_nuevo'),
		url(r'^inicio/menu-plazas/cambiar-plaza/(?P<plaza_id>\d+)/$', 'view_plazas_editar', name='vista_plazas_editar'),
		url(r'^inicio/menu-plazas/eliminar-plaza/(?P<plaza_id>\d+)/$', 'view_plazas_eliminar', name='vista_plazas_eliminar'),
		url(r'^inicio/menu-plazas/listar-plazas$', 'view_plazas_listar', name='vista_plazas_listar'),
)