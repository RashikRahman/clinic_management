from django.shortcuts import render

# Patients View

def patients(request):
    return render(request, 'patients.html')