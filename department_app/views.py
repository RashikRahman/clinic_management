from django.shortcuts import render
from .models import Department

# Department View
def department(request):
    d = Department.objects.all()
    context = {'department': d}
    return render(request, 'department.html',context)
