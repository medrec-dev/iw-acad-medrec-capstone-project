from django.contrib import admin
from .models import DoctorInfo,PatientInfo,Appointment
admin.site.register(DoctorInfo)
admin.site.register(PatientInfo)
admin.site.register(Appointment)
