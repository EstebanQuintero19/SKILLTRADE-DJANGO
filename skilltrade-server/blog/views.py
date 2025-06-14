from django.shortcuts import render

def inicio(request):
    """
    Vista para la página principal del blog.
    Renderiza el template index.html
    """
    return render(request, 'blog/index.html')

def contacto(request):
    """
    Vista para la página de contacto.
    Renderiza el template contacto.html
    """
    return render(request, 'blog/contacto.html')

def galeriavideos(request):
    """
    Vista para la galería de videos.
    Renderiza el template galeria.html
    """
    return render(request, 'blog/galeria.html')