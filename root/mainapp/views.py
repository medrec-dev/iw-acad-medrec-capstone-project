from django.shortcuts import render, HttpResponse

# Create your views here.

#def home(request):
    #return HttpResponse("The content is being displayed from [mainapp->view.py]")

def home(request):
    return render(request,"index.html")

def test(request):
    return HttpResponse("This test is displayed from [mainapp->view.py]")

def app(request):
    return HttpResponse("This is app from [mainapp->view.py]")