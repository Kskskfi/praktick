from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
   return render(request, 'main/profile.html')

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')