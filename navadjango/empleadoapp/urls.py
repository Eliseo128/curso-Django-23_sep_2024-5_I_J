from django.urls import path

from empleadoapp.views import index_empleadoapp

urlpatterns = [
    
    path('',index_empleadoapp) #127.0.0.1:8000
]