from django.contrib import admin
from django.urls import path, include
from mainapp.views import Index, About, Contact, Login, Logout_admin, View_Doctor
#from root.mainapp import views
#from _ast import Index
urlpatterns = [
    path('', Index, name='home'),
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
]