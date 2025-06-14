from django.urls import path
from .views import inicio, contacto, galeriavideos

app_name = 'blog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('quienes-somos/', galeriavideos, name='galeriavideos'),
] 