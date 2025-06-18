from django.shortcuts import render

# Create your views here.

def inicio(request):
    """
    Vista para la página de inicio del portafolio.
    Renderiza el template inicio.html
    """
    context = {
        'nombre': 'Juan Pérez',
        'titulo': 'Desarrollador Full Stack',
        'descripcion': 'Apasionado por crear soluciones web innovadoras y experiencias de usuario excepcionales.',
        'habilidades': ['Python', 'Django', 'JavaScript', 'React', 'HTML/CSS', 'SQL'],
        'experiencia': '5 años',
        'proyectos_completados': 25
    }
    return render(request, 'portafolio/inicio.html', context)

def proyectos(request):
    """
    Vista para la página de proyectos del portafolio.
    Renderiza el template proyectos.html
    """
    proyectos_lista = [
        {
            'titulo': 'E-commerce Platform',
            'descripcion': 'Plataforma de comercio electrónico completa con Django y React.',
            'tecnologias': ['Django', 'React', 'PostgreSQL', 'Stripe'],
            'imagen': 'ecommerce.jpg',
            'url': 'https://github.com/usuario/ecommerce',
            'demo': 'https://demo-ecommerce.com'
        },
        {
            'titulo': 'Task Management App',
            'descripcion': 'Aplicación de gestión de tareas con funcionalidades avanzadas.',
            'tecnologias': ['Django', 'JavaScript', 'Bootstrap', 'SQLite'],
            'imagen': 'taskapp.jpg',
            'url': 'https://github.com/usuario/taskapp',
            'demo': 'https://demo-taskapp.com'
        },
        {
            'titulo': 'Blog Personal',
            'descripcion': 'Blog personal con sistema de gestión de contenido.',
            'tecnologias': ['Django', 'HTML/CSS', 'JavaScript', 'SQLite'],
            'imagen': 'blog.jpg',
            'url': 'https://github.com/usuario/blog',
            'demo': 'https://mi-blog.com'
        },
        {
            'titulo': 'Weather Dashboard',
            'descripcion': 'Dashboard del clima con API de datos meteorológicos.',
            'tecnologias': ['Python', 'Flask', 'JavaScript', 'Chart.js'],
            'imagen': 'weather.jpg',
            'url': 'https://github.com/usuario/weather',
            'demo': 'https://demo-weather.com'
        }
    ]
    
    context = {
        'proyectos': proyectos_lista,
        'total_proyectos': len(proyectos_lista)
    }
    
    return render(request, 'portafolio/proyectos.html', context)

def contacto(request):
    """
    Vista para la página de contacto del portafolio.
    Renderiza el template contacto.html
    """
    context = {
        'email': 'juan.perez@email.com',
        'telefono': '+52 123 456 7890',
        'ubicacion': 'Ciudad de México, México',
        'redes_sociales': {
            'github': 'https://github.com/juanperez',
            'linkedin': 'https://linkedin.com/in/juanperez',
            'twitter': 'https://twitter.com/juanperez',
            'instagram': 'https://instagram.com/juanperez'
        }
    }
    
    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario de contacto
        context['mensaje_enviado'] = True
        context['nombre_contacto'] = request.POST.get('nombre', '')
    
    return render(request, 'portafolio/contacto.html', context)
