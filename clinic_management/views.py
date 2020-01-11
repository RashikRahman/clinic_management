from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def department(request):
    return render(request, 'department.html')

def login(request):
    return render(request, 'login.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def patients(request):
    return render(request, 'patients.html')

def addpatient(request):
    return render(request, 'addpatient.html')

def tests(request):
    return render(request, 'tests.html')
