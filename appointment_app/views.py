from django.shortcuts import render, redirect
from . models import docavailability, appointment
from datetime import  date
# home View.
def home(request):
    #print(date.today())
    doc = docavailability.objects.all()
    context = {'doctor': doc}
    return render(request, 'index.html', context)

def addappointment(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('phone')
        l = request.POST.get('ltd')
        m = request.POST.get('msg')
        a_obj = appointment(name=n, phone=p, ltd=l, msg=m)
        a_obj.save()
        return redirect('/')
    else:
        return redirect('/')

def seeappointment(request):
    d = appointment.objects.all()
    serial = list()
    for i in range(1, len(d) + 1):
        serial.append(i)
    foo = zip(d, serial)
    context = {'appointment': foo}
    return render(request, 'appointment.html', context)


def edit_appointment(request, id):
    app = appointment.objects.get(id=id)
    if request.method == 'POST':
        app.name = request.POST.get('pname')
        app.phone = request.POST.get('pphone')
        app.ltd = request.POST.get('pltd')
        app.msg = request.POST.get('pmsg')
        app.visited = request.POST.get('pvisit')
        app.save()
        return redirect('/seeappointment/')
    return render(request, 'modappointment.html', {'appointment': app})

def remove_appointment(request, id):
    appointment.objects.filter(id=id).delete()
    return redirect('/seeappointment/')
