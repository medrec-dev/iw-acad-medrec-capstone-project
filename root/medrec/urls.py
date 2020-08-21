from django.contrib import admin
from django.urls import path, include
from mainapp.views import About, Index
from _ast import Index
#from mainapp.views import About, Index, Login
urlpatterns = [
    path('', Index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    #path('', include('mainapp.urls')),
]