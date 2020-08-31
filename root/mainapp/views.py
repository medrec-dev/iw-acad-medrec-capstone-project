from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'mainapp/index.html')

def aboutus_view(request):
    return render(request, 'mainapp/aboutus.html')



