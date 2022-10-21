from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['user']

class AppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields = '__all__'



class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length= 255, required=True)
    last_name = forms.CharField(max_length= 255, required=True)
    email = forms.CharField(max_length= 255, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']