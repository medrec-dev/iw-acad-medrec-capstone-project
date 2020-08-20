from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name ="homepage"),
    path('create', views.create, name="createpage")
]