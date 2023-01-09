from django.shortcuts import render
from .models import Users, Avatar
from django.http import HttpResponse

from django.urls import reverse_lazy

from blogapp.forms import RegisterForm, UserEditForm, AvatarForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases class.
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones def.

# Create your views here.

from django.shortcuts import render

def inicio(request):
    lista=Avatar.objects.filter(user=request.user)
    return render(request, 'blogapp/inicio.html', {'imagen':obtenerAvatar(request)})

def login(request):
    return render(request, 'blogapp/login.html')

def logout(request):
    return render(request, 'blogapp/logout.html')

def register(request):
    return render(request, 'blogapp/register.html')

def messages(request):
    return render(request, 'blogapp/messages.html')

def users(request):
    users = users(nombre='Python', apellido='JEjeje', email='242121421@gmail.com')
    users.save
    cadena_texto = 'Usuario guardado: '+users.nombre+' '+users.apellido+' '+users.email
    return HttpResponse(cadena_texto)

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
         imagen=lista[0].imagen.url
    else:
            imagen='media/avatares/avatarpordefecto.png'
    return imagen