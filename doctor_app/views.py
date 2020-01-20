from django.shortcuts import render

# Doctors View
def doctors(request):
    return render(request, 'doctors.html')
