from django.db import models
from doctor_app.models import Doctor

# Patient Model.

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=512)
    gender = models.CharField(max_length=512)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200,default='')
    date = models.DateTimeField()
    is_visited = models.BooleanField(default=False)

    def __str__(self):
        return self.name
