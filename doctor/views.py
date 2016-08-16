from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from doctor.models import Patient
from practitioner.models import Practitioner
from django.http import HttpResponse
from forms import PatientForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


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