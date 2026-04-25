from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import make_password, check_password

def default(request):
    return redirect('welcome')

def welcome(request):
    return render(request, 'welcome.html') 

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

