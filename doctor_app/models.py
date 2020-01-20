from django.db import models
from department_app.models import Department

# Doctor Model
class Doctor(models.Model):
    department = models.ForeignKey(Department, related_name='doctors', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    email = models.EmailField(default='')
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.name


