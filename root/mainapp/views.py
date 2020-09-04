from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *
#from mainapp.views import About, Index, Login

def About(request):
    return render(request,'about.html')

def Index(request):
    if not request.user.is_authenticated:
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
            if user.is_authenticated:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except: 
                error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login')
def create(request):
    return render(request,'create.html')

def listPatients(request):
    return render (request,'mainapp/patient-list.html')

def View_Doctor(request):
    if not request.user.is_authenticated    :
        return redirect('login')
    #logout(request)
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html',d)

def View_Patient(request):
    if not request.user.is_authenticated:
        return redirect('login')
    #logout(request)
    pat = Patient.objects.all()
    p = {'pat':pat}
    return render(request, 'view_patient.html',p)

def Delete_Doctor(request,did):
    if not request.user.is_authenticated:
        return redirect('login')
    doctor = Doctor.objects.get(id=did)
    doctor.delete()
    return redirect('view_doctor')

def Delete_Patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.get(patient_id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
<<<<<<< HEAD
    #if request.user.is_superuser:
        if request.method == 'POST':
            fn = request.POST['fname']  # The name mentioned in the text box should be mentioned here
            e = request.POST['email']
            dob = request.POST['dob']
            gen = request.POST['gender']
            try:
                Patient.objects.create(
                    patient_firstName=fn,
                    patient_email=e,
                    patient_dob=dob,
                    patient_gender=gen,
                )
                error = "no"
            except Exception as e:
                print(e)
                error = "yes"
        p = {'error': error}
        return render(request, 'add_patient.html', p)

||||||| 2a5df66... fix: Patient adding and deletion resolved
    if request.method == 'POST':
        fn = request.POST['fname']  # The name mentioned in the text box should be mentioned here
        e = request.POST['email']
        dob = request.POST['dob']
        gen = request.POST['gender']
        try:
            Patient.objects.create(
                patient_firstName=fn,
                patient_email=e,
                patient_dob=dob,
                patient_gender=gen,
            )
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    p = {'error': error}
    return render(request, 'add_patient.html', p)

=======
    if request.method=='POST':
        fn = request.POST['fname'] # The name mentioned in the text box should be mentioned here
        e = request.POST['email']
        try:
            Patient.objects.create( patient_firstName=fn,patient_email=e )
            error = "no"
        except: 
            error = "yes"
    p = {'error':error}
    return render(request,'add_patient.html',p)
>>>>>>> parent of 2a5df66... fix: Patient adding and deletion resolved

def Add_Doctor(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name'] # The name mentioned in the text box should be mentioned here
        c = request.POST['contact']
        try:
            Doctor.objects.create(doctor_name=n,doctor_contact=c )
            error = "no"
        except: 
                error = "yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def Profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
<<<<<<< HEAD
    return render(request, 'profile.html')

def Edit_Doctor(request, did):  
    if not request.user.is_authenticated:
        return redirect('login')
    doctor = Doctor.objects.get(id=did)
    return render(request,'edit_doctor.html', {'doctor':doctor})  

def Edit_Patient(request, pid):  
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.get(patient_id=pid)
    return render(request,'edit_patient.html', {'patient':patient})  
||||||| 2a5df66... fix: Patient adding and deletion resolved
    return render(request, 'profile.html')
=======
    return render(request,'profile.html')
>>>>>>> parent of 2a5df66... fix: Patient adding and deletion resolved
