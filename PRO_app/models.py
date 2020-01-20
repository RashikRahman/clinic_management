from django.db import models


# Create your models here.
class Student(models.Model):
   name = models.CharField(max_length=100, default="")
   student_ID = models.IntegerField(default=0)
   email_address = models.CharField(max_length=500, default="")

   def __str__(self):
      return self.name
