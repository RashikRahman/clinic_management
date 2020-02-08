
from django.db import models
from patient_app.models import Patient
from services_app.models import Service
import datetime
# Invoice Model


class Invoice(models.Model):
    PatientName = models.OneToOneField(Patient, related_name='invoice', on_delete=models.CASCADE)
    ServiceName = models.ForeignKey(Service,  on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    Sub_Total = models.IntegerField(default=0)
    Discount = models.IntegerField(default=0)
    Total_Amount = models.IntegerField(default=0)
    Total_Paid = models.IntegerField(default=0)
    Total_Due = models.IntegerField(default=0)
    Due_Status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.PatientName)


