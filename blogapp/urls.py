from django.urls import path
from blogapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('messages/', messages, name='messages'),
    path('users/', users, name='users'),


    #path('users/list/', UserList.as_view(), name='userlist'),
]   