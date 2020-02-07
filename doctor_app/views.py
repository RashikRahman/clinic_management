from django.shortcuts import render,redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Doctors View
def doctors(request):
    doc = Doctor.objects.all()
    context = {'doctor': doc}
    return render(request, 'doctors.html',context)



def AddDoc(request):

    if request.method == 'POST':
        dp = request.POST.get('ddep')
        n = request.POST.get('dname')
        p = request.POST.get('dmob')
        e = request.POST.get('demail')
        d = request.POST.get('ddes')

        d_obj = Doctor(department=dp,name=n,phone=p,email=e,description=d)
        d_obj.save()
        return redirect('/doctors/')
    else:
        return redirect('/doctors/')