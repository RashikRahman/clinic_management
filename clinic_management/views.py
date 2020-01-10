from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def department(request):
    return render(request, 'department.html')

def login(request):
    return render(request, 'login.html')

def services(request):
    return render(request, 'services.html')
