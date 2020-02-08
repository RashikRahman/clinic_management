from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Invoice

@login_required(login_url="/")
# invoice views here.

def invoice (request):
    i = Invoice.objects.all()
    context = {'invc': i}
    return render(request, 'invoice.html',context)

def AddInvc(request):
    if request.method == 'POST':
        pn = request.POST.get('pname')
        sn = request.POST.get('servc')
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
