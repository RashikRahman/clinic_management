from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from patient_app.models import Patient
from doctor_app.models import Doctor

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
        doctor = Doctor.objects.get(name=doc)
        bool=True
        if dia=='False':
            bool=False
        elif dia == 'True':
            bool=True

        p_obj = Patient(doctor=doctor, name=pn, age=ag, gender=gn, phone=mb, address=ad, MedNAme=med, complain=cmp,
                        observation=obs, advice=adv, dose=ds, duration=dr, diabetes=bool, blood_group=bl)
        p_obj.save()
        return redirect('/patients/')
    else:
        return redirect('/patients/')


def remove_patient(request,id):
    Patient.objects.filter(id=id).delete()
    return redirect('/patients/')

def edit_patient(request,id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST.get('pname')
        patient.age = request.POST.get('page')
        patient.gender = request.POST.get('pgender')
        patient.phone = request.POST.get('pmob')
        patient.address = request.POST.get('paddress')
        patient.doctor = Doctor.objects.get(name=request.POST.get('pdoc'))
        patient.complain = request.POST.get('pcomp')
        patient.observation = request.POST.get('pobs')
        patient.advice = request.POST.get('padvc')
        patient.MedNAme = request.POST.get('pmed')
        patient.dose= request.POST.get('pdose')
        patient.duration = request.POST.get('pdur')
        dia = request.POST.get('pdia')
        patient.blood_group = request.POST.get('pblood')

        bool = True
        if dia == 'False':
            bool = False
        elif dia == 'True':
            bool = True

        patient.diabetes=bool


        patient.save()
        return redirect('/patients/')


    return render(request, 'modpatient.html', {'patient': patient})