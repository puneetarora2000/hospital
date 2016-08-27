from django.conf.urls import patterns, include, url
from autofixture import generators, register, AutoFixture

#AutoFixture.autodiscover()

#http://stackoverflow.com/questions/12807220/why-isnt-admin-autodiscover-called-automatically-in-django-when-using-the-adm

urlpatterns = patterns(
	'',
	url(r'(?P<doctor_id>\d+)/all/$', 'doctor.views.patients'),
	url(r'(?P<doctor_id>\d+)/get/(?P<patient_id>\d+)/$', 'doctor.views.patient'),
	url(r'(?P<doctor_id>\d+)/create/$', 'doctor.views.create'),
	
	)