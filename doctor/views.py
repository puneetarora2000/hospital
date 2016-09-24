from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from doctor.models import Patient,RegisterDevicesForPatient
from practitioner.models import Practitioner
from django.http import HttpResponse
from forms import PatientForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import  User, Group
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics

from doctor.serializers import *


# Create your views here.

def patients(request, doctor_id=1):
	args = {}
	args.update(csrf(request))
	args['doctor'] = doctor_id
	args['patients'] = Patient.objects.filter( Doctor_Visited_Id = doctor_id)
	return render_to_response('patients.html',
		args )


def patient(request, doctor_id=1 , patient_id=1):
	return render_to_response('patient.html', 
		{'patient': Patient.objects.get(id = patient_id), 'practitioner': Practitioner.objects.get(id = doctor_id)})


def create(request, doctor_id=1):
	if request.POST:
		form = PatientForm(request.POST, request.FILES)
		form.instance.Doctor_Visited_Id = doctor_id
		if form.is_valid():
			form.save()
			args = {}
			args['patients'] = Patient.objects.filter( Doctor_Visited_Id = doctor_id)
			return render_to_response('patients.html', args)

	else:
		form = PatientForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['doctor'] = doctor_id
	return render_to_response('create_patient.html', args)

#1
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
#2
class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


#7
class  PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

#Query Based on the doctorid
class PatientListViewSet(viewsets.ModelViewSet):
	serializer_class = PatientSerializer
	def get_queryset(self):
		#usr = self.kwargs['usr']
		try:
			username = self.request.query_params.get('usr', None)
			print username
			userObj = User.objects.get(username=username)
		except User.DoesNotExist:
			userObj = None
		return Patient.objects.filter(DoctorID=userObj)

		# else:
		# return Patient.objects.all()

#7
class  RegisterDevicesForPatientViewSet(viewsets.ModelViewSet):
	queryset = RegisterDevicesForPatient.objects.all()
	serializer_class = RegisterDevicesForPatientSerializer


#InsuranceCompanySerializer

class  InsuranceCompanyViewSet(viewsets.ModelViewSet):
	queryset = InsuranceCompany.objects.all()
	serializer_class = InsuranceCompanySerializer

#PatientHealthData

class  PatientHealthDataViewSet(viewsets.ModelViewSet):
	queryset = PatientHealthData.objects.all()
	serializer_class = PatientHealthDataSerializer