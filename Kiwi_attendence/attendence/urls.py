from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.LoginPage, name='login'),
    path('attendence', views.EmployeeAttendence, name='attendence'),
    path('register', views.Register, name='register'),
    path('adduser', views.AddUser, name='adduser')
]