from django.urls import path
from .views import inicio, contacto, galeriavideos

app_name = 'blog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeriavideos, name='galeriavideos'),
    path('index/', inicio, name='index'), 
] 