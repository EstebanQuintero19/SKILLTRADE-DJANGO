from django.urls import path
from .views import inicio, proyectos, contacto

app_name = 'portafolio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('proyectos/', proyectos, name='proyectos'),
    path('contacto/', contacto, name='contacto'),
] 