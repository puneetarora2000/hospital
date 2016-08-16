from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	(r'^all_med/$','inventory.views.display_all_medicines'),
	(r'^get_med/(?P<med_name>\w+)/$','inventory.views.display_medicine'),
	(r'^create/$', 'inventory.views.create'),

	) 