from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Invoice
from patient_app.models import Patient
from services_app.models import Service

@login_required(login_url="/")
# invoice views here.

def invoice (request):
    i = Invoice.objects.all()
    serial = list()
    for j in range(1, len(i) + 1):
        serial.append(j)
    foo = zip(i, serial)
    context = {'invc': foo}
    return render(request, 'invoice.html',context)

def AddInvc(request):
    if request.method == 'POST':
        pn = Patient.objects.get(name=request.POST.get('pname'))
        sn = Service.objects.get(name=request.POST.get('servc'))
        stl = request.POST.get('sttl')
        ds = request.POST.get('dis')
        tla = request.POST.get('ttlamnt')
        tlp = request.POST.get('ttlpaid')
        tld = request.POST.get('ttldue')
        du = request.POST.get('due')
        bool=True
        if du=='False':
            bool=False
        elif du == 'True':
            bool=True


        i_obj = Invoice(PatientName=pn, ServiceName=sn, Sub_Total=stl, Discount=ds,Total_Amount=tla,Total_Paid=tlp,Total_Due=tld,Due_Status=bool)
        i_obj.save()
        return redirect('/invoice/')
    else:
        return redirect('/invoice/')


def remove_invoice(request,id):
    Invoice.objects.filter(id=id).delete()
    return redirect('/invoice/')


def edit_invoice(request,id):
    invoice = Invoice.objects.get(id=id)
    if request.method == 'POST':
        invoice.PatientName = Patient.objects.get(name=request.POST.get('pname'))
        invoice.ServiceName = Service.objects.get(name=request.POST.get('servc'))
        invoice.Sub_Total = request.POST.get('sttl')
        invoice.Discount = request.POST.get('dis')
        invoice.Total_Amount = request.POST.get('ttlamnt')
        invoice.Total_Paid = request.POST.get('ttlpaid')
        invoice.Total_Due = request.POST.get('ttldue')
        du = request.POST.get('due')
        bool = True
        if du == 'False':
            bool = False
        elif du == 'True':
            bool = True

        invoice.Due_Status=bool
        invoice.save()
        return redirect('/invoice/')
    return render(request, 'modinvoice.html', {'invc': invoice})