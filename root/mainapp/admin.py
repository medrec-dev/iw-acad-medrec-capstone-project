from django.contrib import admin
# from .models import Doctor,Patient,Appointment --> OPTIONAL
from .models import *
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
