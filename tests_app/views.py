from django.shortcuts import render
from .models import Test
# Tests view

def tests(request):
    t = Test.objects.all()
    context = {'test': t}
    return render(request,'tests.html',context)
