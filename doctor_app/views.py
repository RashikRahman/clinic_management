from django.shortcuts import render
from .models import Doctor

# Doctors View
def doctors(request):
    doc = Doctor.objects.all()
    context = {'doctor': doc}
    return render(request, 'doctors.html',context)
