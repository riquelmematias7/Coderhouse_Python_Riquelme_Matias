from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña.', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña.', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}# Para cada campo le asigna un valor vacio.

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña.', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña.', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}# Para cada campo le asigna un valor vacio.

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='Imagen')