from django.shortcuts import render,redirect
from .models import Department
from django.contrib.auth.decorators import login_required

# Department View


@login_required(login_url="/")
def department(request):

    d = Department.objects.all()
    context = {'department': d}
    return render(request, 'department.html',context)


def AddDept(request):

    if request.method == 'POST':
        n = request.POST.get('dname')
        d_obj = Department(name=n)
        d_obj.save()
        return redirect('/department/')
    else:
        return redirect('/department/')
