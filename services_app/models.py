from django.db import models
from department_app.models import Department

# Service Model

class Service(models.Model):
    department = models.ForeignKey(Department, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    cost = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name
