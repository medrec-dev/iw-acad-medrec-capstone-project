from django.contrib import admin
from django.urls import path, include
from mainapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('', include('mainapp.urls')),
]
