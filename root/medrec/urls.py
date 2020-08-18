"""medrec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('mainapp.urls')),
    path('test', include('mainapp.urls')),
    path('app', include('mainapp.urls'))
||||||| b8006c0
    path('mainapp/', include('mainapp.urls')),
=======
    path('', include('mainapp.urls')),
>>>>>>> 83fc352db06cec65ae3e01869e3144e5c99921af
]
