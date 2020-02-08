from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from patient_app.models import Patient

@login_required(login_url="/")
# AddPatients View
def addpatient(request):
    return render(request, 'addpatient.html')


def addpatients(request):
    if request.method == 'POST':
        pn = request.POST.get('pname')
        ag = request.POST.get('page')
        gn = request.POST.get('pgender')
        mb = request.POST.get('pmob')
        ad = request.POST.get('paddress')
        doc = request.POST.get('pdoc')
        cmp = request.POST.get('pcomp')
        obs = request.POST.get('pobs')
        adv = request.POST.get('padvc')
        med = request.POST.get('pmed')
        ds = request.POST.get('pdose')
        dr = request.POST.get('pdur')
        dia = request.POST.get('pdia')
        bl = request.POST.get('pblood')

        bool=True
        if dia=='False':
            bool=False
        elif dia == 'True':
            bool=True

        p_obj = Patient(doctor=doc, name=pn, age=ag, gender=gn, phone=mb, address=ad, MedNAme=med, complain=cmp,
                        observation=obs, advice=adv, dose=ds, duration=dr, diabetes=bool, blood_group=bl)
        p_obj.save()
        return redirect('/patients/')
    else:
        return redirect('/patients/')

