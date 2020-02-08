from django.shortcuts import render,redirect
from .models import Department
from django.contrib.auth.decorators import login_required

# Department View


@login_required(login_url="/")
def department(request):
    d = Department.objects.all()
    serial = list()
    for i in range(1, len(d)+1):
        serial.append(i)
    foo = zip(d, serial)
    context = {'department': foo}
    return render(request, 'department.html',context)


def AddDept(request):

    if request.method == 'POST':
        n = request.POST.get('dname')
        d_obj = Department(name=n)
        d_obj.save()
        return redirect('/department/')
    else:
        return redirect('/department/')


def removedepartment(request,id):
    Department.objects.filter(id=id).delete()
    return redirect('/department/')


