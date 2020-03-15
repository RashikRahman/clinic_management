from django.shortcuts import render,redirect
from  . models import docavailability

# home View.
def home(request):
    doc = docavailability.objects.all()
    context = {'doctor': doc}
    return render(request, 'index.html', context)

