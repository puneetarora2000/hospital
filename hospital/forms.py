from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

	def setID(self, ID):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.username = ID

	def setName(self, name):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.first_name = name
