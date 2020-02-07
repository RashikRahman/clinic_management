from django.db import models
from doctor_app.models import Doctor
import datetime
# Patient Model.




class Patient (models.Model):

    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=512)
    gender = models.CharField(max_length=512)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, default='')
    MedNAme = models.CharField(max_length=300, default='')
    complain = models.TextField(max_length=250, default='')
    observation = models.TextField(max_length=250, default='')
    advice = models.CharField(max_length=200, default='')
    dose = models.CharField(max_length=20, default='')
    duration = models.CharField(max_length=20, default='')
    date = models.DateTimeField(default=datetime.datetime.now())
    diabetes = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name