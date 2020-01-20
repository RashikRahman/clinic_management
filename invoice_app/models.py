
from django.db import models
from patient_app.models import Patient
from services_app.models import Service

# Invoice Model


class Invoice(models.Model):
    PatientName = models.OneToOneField(Patient, related_name='invoice', on_delete=models.CASCADE)
    ServiceName = models.ForeignKey(Service,  on_delete=models.CASCADE)
    Sub_Total = models.IntegerField(default=0)
    Discount = models.IntegerField(default=0)
    Total_Amount = models.IntegerField(default=0)
    Total_Paid = models.IntegerField(default=0)
    Due = models.BooleanField(default=False)
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.pk


