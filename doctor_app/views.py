from django.shortcuts import render,redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required
from department_app.models import Department

@login_required(login_url="/")
# Doctors View
def doctors(request):
    doc = Doctor.objects.all()
    serial = list()
    for i in range(1, len(doc) + 1):
        serial.append(i)
    foo = zip(doc, serial)
    context = {'doctor': foo}
    return render(request, 'doctors.html',context)



def AddDoc(request):

    if request.method == 'POST':
        dp = request.POST.get('ddep')
        n = request.POST.get('dname')
        p = request.POST.get('dmob')
        e = request.POST.get('demail')
        d = request.POST.get('ddes')
        department = Department.objects.get(name=dp)

        d_obj = Doctor(department=department,name=n,phone=p,email=e,description=d)
        d_obj.save()
        return redirect('/doctors/')
    else:
        return redirect('/doctors/')


def remove_doc(request,id):
    Doctor.objects.filter(id=id).delete()
    return redirect('/doctors/')


def edit_doc(request,id):
    doc = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doc.name = request.POST.get('dname')
        department = Department.objects.get(name=request.POST.get('ddep'))
        doc.department = department
        doc.phone = request.POST.get('dmob')
        doc.email = request.POST.get('demail')
        doc.description=request.POST.get('ddes')
        doc.save()
        return redirect('/doctors/')
    return render(request, 'moddoc.html', {'doctors': doc})