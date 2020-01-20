from django.shortcuts import render

# invoice views here.

def invoice (request):
    return render(request, 'invoice.html')
