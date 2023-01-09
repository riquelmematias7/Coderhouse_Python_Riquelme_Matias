from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('', inicio, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('messages/', messages, name='messages'),
]   