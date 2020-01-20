from django.shortcuts import render

# Services View
def services(request):
    return render(request, 'services.html')
