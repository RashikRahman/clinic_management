from django.shortcuts import render

# Department View
def department(request):
    return render(request, 'department.html')
