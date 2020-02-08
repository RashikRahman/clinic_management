from django.shortcuts import render,redirect
from .models import Service
from django.contrib.auth.decorators import login_required
from department_app.models import Department

@login_required(login_url="/")
# Services View
def services(request):
    s = Service.objects.all()
    serial = list()
    for i in range(1, len(s) + 1):
        serial.append(i)
    foo = zip(s, serial)
    context = {'service': foo}
    return render(request, 'services.html', context)



def AddSer(request):

    if request.method == 'POST':
        n = request.POST.get('sname')
        c = request.POST.get('scost')
        du = request.POST.get('sdur')
        dp = request.POST.get('sdp')

        department = Department.objects.get(name=dp)

        s_obj = Service(name=n,cost=c,duration=du,department=department)
        s_obj.save()
        return redirect('/services/')
    else:
        return redirect('/services/')

# Remove Services view
def remove_service(request, id):
    Service.objects.filter(id=id).delete()
    return redirect('/services/')


def edit_service(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('sname')
        department = Department.objects.get(name=request.POST.get('sdp'))
        service.department = department
        service.cost = request.POST.get('scost')
        service.duration = request.POST.get('sdur')
        service.save()
        return redirect('/services/')
    return render(request, 'modservice.html', {'service': service})