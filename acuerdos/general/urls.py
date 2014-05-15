from django.conf.urls import patterns, url

urlpatterns=patterns('acuerdos.general.views', 
		url(r'^$', 'view_login', name='vista_principal'),
		url(r'^inicio/$', 'view_index', name='vista_inicio'),
		url(r'^accounts/login/$', 'view_logout', name='vista_login'),
		url(r'^accounts/logout/$', 'view_logout', name='vista_logout'),
)