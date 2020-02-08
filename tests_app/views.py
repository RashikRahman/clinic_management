from django.shortcuts import render,redirect
from .models import Test
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
# Tests view

def tests(request):
    t = Test.objects.all()
    serial = list()
    for i in range(1, len(t) + 1):
        serial.append(i)
    foo = zip(t, serial)
    context = {'test': foo}
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


def remove_test(request,id):
    Test.objects.filter(id=id).delete()
    return redirect('/tests/')


def edit_test(request,id):
    test = Test.objects.get(id=id)
    if request.method == 'POST':
        test.name = request.POST.get('tname')
        test.price = request.POST.get('tprc')
        test.save()
        return redirect('/tests/')
    return render(request, 'modtest.html', {'tests': test})