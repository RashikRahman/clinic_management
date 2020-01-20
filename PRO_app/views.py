from django.shortcuts import render
from .models import Student

# PRo View
def show(request):
    s = Student.objects.all()
    context = {'student': s}
    return render(request, 'bdpro.html',context)

def addstudent(request):

    print(request)

    n=request.POST.get('NAME')
    s = request.POST.get('SID')
    e = request.POST.get('EMAIL')

    print(n,s,e)

    s_obj=Student(name=n, student_ID = s, email_address = e)
    s_obj.save()

    s = Student.objects.all()
    conext = {'student': s}
    return render(request, 'bdpro.html', conext)
