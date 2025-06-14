from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('<h1>Bienvenido a mi Blog</h1>')

def contacto(request):
    return HttpResponse('<p>Contáctanos en: correo@ejemplo.com</p>')

def galeriavideos(request):
    return HttpResponse("enlaces de videos a youtube")
