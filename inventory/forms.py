from django import forms
from models import Medicines


class MedicinesForm(forms.ModelForm):

	class Meta:
		model = Medicines
		fields = ('medicine_name', 'expiry_date', 'price', 'quantity')


# class GetMedicine(forms.ModelForm):
# 	class Meta:
# 		model = Medicines
# 		fields = ('medicine_name')