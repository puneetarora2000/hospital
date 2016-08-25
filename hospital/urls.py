"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import url, include
from rest_framework import routers
from doctor  import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet),
router.register(r'groups', views.GroupViewSet),
router.register(r'patients', views. PatientViewSet)
router.register(r'patientsdevices', views. RegisterDevicesForPatientViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^appointments/', include('appointments.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^doctor/', include('doctor.urls')),
    url(r'^pharmacist/', include('pharmacist.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^accounts/login/$', 'hospital.views.login'),
    url(r'^accounts/auth/$', 'hospital.views.auth_view'),
    url(r'^accounts/logout/$', 'hospital.views.logout'),
    url(r'^accounts/loggedin/$', 'hospital.views.loggedin'),
    url(r'^accounts/invalid/$', 'hospital.views.invalid_login'),
    url(r'^accounts/register/$', 'hospital.views.register_user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)







