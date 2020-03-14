from django.shortcuts import render,redirect
from django.contrib.auth.forms import authenticate
from django.contrib.auth import login,logout


# home View.
def home(request):
    return render(request,'index.html')
