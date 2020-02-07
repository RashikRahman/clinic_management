from django.shortcuts import render,redirect
from .models import Service
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Services View
def services(request):
    s = Service.objects.all()
    context = {'service': s}
    return render(request, 'services.html', context)



def AddSer(request):

    if request.method == 'POST':
        n = request.POST.get('sname')
        c = request.POST.get('scost')
        du = request.POST.get('sdur')
        dp = request.POST.get('sdp')

        s_obj = Service(name=n,cost=c,duration=du,department=dp)
        s_obj.save()
        return redirect('/services/')
    else:
        return redirect('/services/')