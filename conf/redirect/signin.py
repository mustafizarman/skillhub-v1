from django.contrib.auth import logout, login
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home') 

def login_view(request):
    login(request)
    return redirect('')