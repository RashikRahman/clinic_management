from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,authenticate
from django.contrib.auth import login,logout


# Login View.


def logins(request):

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        form = AuthenticationForm(data=request.POST)
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html')


def lougts(request):

    if request.method == 'POST':
     logout(request)
     return redirect('/')
