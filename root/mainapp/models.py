from django.db import models
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
    return self.patient_email
