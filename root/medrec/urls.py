from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

#from root.mainapp import views
#from _ast import Index
urlpatterns = [
    #path('', Index, name='create'),
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    #path('', include('mainapp.urls')),
]