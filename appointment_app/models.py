from django.db import models

class appointment(models.Model):
    name = models.CharField(max_length=255,default='')
    phone = models.IntegerField(default=0)
    ltd = models.CharField(max_length=255, default='')
    msg = models.TextField(max_length=700, default='')
    visited = models.CharField(max_length=255, default='No')

    def __str__(self):
        return self.name

class docavailability(models.Model):
    Location = models.CharField(max_length=255,default='')
    day = models.CharField(max_length=255,default='')
    time = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.day
