from django.shortcuts import render,redirect
from .models import Test
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Tests view

def tests(request):
    t = Test.objects.all()
    context = {'test': t}
    return render(request,'tests.html',context)


def AddTest(request):

    if request.method == 'POST':
        n = request.POST.get('tname')
        p = request.POST.get('tprc')

        d_obj = Test(name=n,price=p)
        d_obj.save()
        return redirect('/tests/')
    else:
        return redirect('/tests/')
