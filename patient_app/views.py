from django.shortcuts import render
from .models import Patient
# Patients View

def patients(request):
    p = Patient.objects.all()
    context = {'patient': p}
    return render(request, 'patients.html',context)