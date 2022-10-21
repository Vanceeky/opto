from django.contrib import admin
from .models import Patient, Appointment

# Register your models here.


admin.site.register(Appointment)
admin.site.register(Patient)
