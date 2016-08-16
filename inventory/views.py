from django.shortcuts import render_to_response
from inventory.models import Medicines
from forms import MedicinesForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render



def home(request):
	return render(request, 'home.html')


def all(request):
	return HttpResponseRedirect('inventory/all_med')

def display_all_medicines(request):
	return render_to_response('all_medicines.html',{'medicines': Medicines.objects.all()})


def display_medicine(request, med_name):
	return render_to_response('medicine.html',{'medicine': Medicines.objects.get(medicine_name = med_name)})


def create(request):
	if request.POST:
		form = MedicinesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	else:
		form = MedicinesForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_medicine.html', args)	