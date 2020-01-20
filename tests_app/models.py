from django.db import models

# Test Model
class Test(models.Model):
    name = models.CharField(max_length=228, default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


