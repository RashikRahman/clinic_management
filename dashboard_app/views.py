from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url="/")
# Home View
def home(request):
    return render(request, 'home.html')