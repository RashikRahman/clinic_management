from django.shortcuts import render

# appointment view.

def appointment(request):
    return render(request,'appointment.html')