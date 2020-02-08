from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Patients View

def patients(request):
    p = Patient.objects.all()
    serial = list()
    for i in range(1, len(p) + 1):
        serial.append(i)
    foo = zip(p, serial)
    context = {'patient': foo}
    return render(request, 'patients.html',context)

def prescribe_view(request, id):
    patient = Patient.objects.get(id=id)

    context = {
        'patient': patient
    }
    return render(request, 'prescription.html', context)