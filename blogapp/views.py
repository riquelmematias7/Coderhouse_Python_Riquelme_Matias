from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

# Create your views here.
def index(request):
    return render(request, 'blogapp/index.html')

def login(request):
    return render(request, 'blogapp/login.html')

def logout(request):
    return render(request, 'blogapp/logout.html')

def register(request):
    return render(request, 'blogapp/register.html')