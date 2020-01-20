from django.shortcuts import render

# Login View.
def login(request):
    return render(request, 'login.html')