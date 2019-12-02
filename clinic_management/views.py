from django.shortcuts import render,HttpResponse

def home(request):
    #return render(request, login.html)
    return HttpResponse('Homepage')