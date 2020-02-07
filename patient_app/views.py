from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Patients View

def patients(request):
    p = Patient.objects.all()
    context = {'patient': p}
    return render(request, 'patients.html',context)