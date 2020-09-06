from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),

    #path('admin/', admin.site.urls),
]