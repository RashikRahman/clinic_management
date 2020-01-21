from django.shortcuts import render
from .models import Service

# Services View
def services(request):
    s = Service.objects.all()
    context = {'service': s}
    return render(request, 'services.html', context)
