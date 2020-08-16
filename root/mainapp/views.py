from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("The content is being displayed from [mainapp->view.py]")
