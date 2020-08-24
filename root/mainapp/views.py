from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
#from mainapp.views import About, Index, Login

def About(request):
    return render(request,'about.html')

def Index(request):
    #if not request.user.is_staff:
        #return redirect('login')
    return render(request,'index.html')

def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "No ERROR"
            else:
                error = "ERROR"
        except:
                error = "ERROR"
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

