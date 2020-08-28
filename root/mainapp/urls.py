from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index, name ="homepage"),
    #path('create', views.create, name="createpage")
    #path('', views.index, name ="Index")
]