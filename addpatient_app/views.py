from django.shortcuts import render

# AddPatients View
def addpatient(request):
    return render(request, 'addpatient.html')