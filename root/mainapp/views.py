from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *
#from mainapp.views import About, Index, Login

def About(request):
    return render(request,'about.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname'] # The name mentioned in the text box should be mentioned here
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except: 
                error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
def create(request):
    return render(request,'create.html')

def listPatients(request):
    return render (request,'mainapp/patient-list.html')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    #logout(request)
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html',d)
