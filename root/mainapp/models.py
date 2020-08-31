from django.db import models
from django.db.models.functions import Concat
import datetime
from django.utils import timezone
#import django.utils.timezone
#default= 2020-09-11
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=25)
    doctor_contact = models.IntegerField()
    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    PATIENT_GENDER = (
        ('F','Female'),
        ('M', 'Male'),
        ('O', 'Others')
    )
    patient_id = models.AutoField(primary_key=True)
    patient_firstName = models.CharField(max_length=25)
    patient_middleName = models.CharField(max_length=25)
    patient_lastName = models.CharField(max_length=25)
    #patient_name = models.CharField(max_length=100)

    #patient_name = patient_firstName + patient_middleName + patient_lastName
    
    patient_email = models.EmailField()
    patient_dob = models.DateField()
    #patient_time = models.TimeField(default=timezone.now)
    #patient_dob = 2020,8,24
    patient_gender = models.CharField(max_length=1, choices=PATIENT_GENDER)

    def __str__(self):
        return self.patient_email

class Appointment(models.Model):
    # doctor = models.ForeignKey(AppointmentInfo,on_delete=models.CASCADE)
    # patient = models.ForeignKey(AppointmentInfo,on_delete=models.CASCADE)
    appoint_date = models.DateField
    appint_time = models.TimeField

    # def __str__(self):
    #     return self.doctor.doctor_name + "---" + self.patient.patient_name
