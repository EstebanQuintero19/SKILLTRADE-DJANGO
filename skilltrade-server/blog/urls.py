from django.urls import path
from .views import (
    inicio, contacto, galeriavideos, servicios, 
    acerca, login, registro, dashboard
)

app_name = 'blog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeriavideos, name='galeriavideos'),
    path('index/', inicio, name='index'),
    path('servicios/', servicios, name='servicios'),
    path('acerca/', acerca, name='acerca'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),
] 