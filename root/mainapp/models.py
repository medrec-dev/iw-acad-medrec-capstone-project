from django.db import models

class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=25)
    doctor_contact = models.IntegerField()
    def __str__(self):
        return self.doctor_name

class PatientInfo(models.Model):
    PATIENT_GENDER = (
        ('F','Female'),
        ('M', 'Male'),
        ('O', 'Others')
    )
    patient_id = models.AutoField(primary_key=True)
    patient_firstName = models.CharField(max_length=25)
    patient_middleName = models.CharField(max_length=25)
    patient_lastName = models.CharField(max_length=25)
    patient_email = models.EmailField()
    patient_dob = models.DateField()
    patient_gender = models.CharField(max_length=1, choices=PATIENT_GENDER)

    def __str__(self):
        return self.patient_email #self.patient_firstName

class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorInfo,on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientInfo,on_delete=models.CASCADE)
    appoint_date = models.DateField
    appint_time = models.TimeField

    def __str__(self):
        return self.doctor.doctor_name + "---" + self.patient.patient_name
