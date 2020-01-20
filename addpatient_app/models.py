
from django.db import models
from patient_app.models import Patient

# Consultancy Model


class Medicine(models.Model):
    pass

''' name = models.CharField(max_length=500 , related_name='medicine')

    def __str__(self):
        return self.name
'''

class AddPatient(models.Model):
    pass
'''PatientName = models.OneToOneField(Patient, related_name='addpatient', on_delete=models.CASCADE)
    MedNAme = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    complain = models.TextField(max_length=250) #add another complain option would be added
    observation = models.TextField(max_length=250)
    advice = models.CharField(max_length=200)
    dose = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    date = models.DateTimeField()
    diabetes = models.BooleanField()
    blood_group = models.CharField(max_length=15)

    def __str__(self):
        return self.pk'''


