from django.shortcuts import render

# Tests view

def tests(request):
    return render(request,'tests.html')
