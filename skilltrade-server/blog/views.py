from django.shortcuts import render
from django.contrib import messages

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

def servicios(request):
    """
    Vista para la página de servicios.
    Renderiza el template servicios.html con contexto dinámico
    """
    servicios_lista = [
        {
            'nombre': 'Intercambio de Habilidades',
            'descripcion': 'Conecta con personas que comparten tus intereses y aprende nuevas habilidades.',
            'icono': 'fas fa-exchange-alt',
            'precio': 'Gratis'
        },
        {
            'nombre': 'Cursos Especializados',
            'descripcion': 'Accede a cursos creados por expertos en diferentes áreas de conocimiento.',
            'icono': 'fas fa-graduation-cap',
            'precio': 'Desde $29.99'
        },
        {
            'nombre': 'Mentoría Personalizada',
            'descripcion': 'Recibe orientación personalizada de mentores experimentados en tu campo.',
            'icono': 'fas fa-user-tie',
            'precio': 'Desde $49.99'
        },
        {
            'nombre': 'Certificaciones',
            'descripcion': 'Obtén certificados reconocidos por completar cursos y programas.',
            'icono': 'fas fa-certificate',
            'precio': 'Desde $19.99'
        }
    ]
    
    context = {
        'servicios': servicios_lista,
        'total_servicios': len(servicios_lista)
    }
    
    return render(request, 'blog/servicios.html', context)

def acerca(request):
    """
    Vista para la página "Acerca de".
    Renderiza el template acerca.html con información de la empresa
    """
    context = {
        'mision': 'Conectar personas a través del intercambio de habilidades y conocimientos, creando una comunidad global de aprendizaje colaborativo.',
        'vision': 'Ser la plataforma líder mundial en el intercambio de habilidades, democratizando el acceso al conocimiento.',
        'valores': [
            'Colaboración y cooperación',
            'Aprendizaje continuo',
            'Diversidad e inclusión',
            'Innovación y creatividad',
            'Integridad y transparencia'
        ],
        'estadisticas': {
            'usuarios': '10,000+',
            'habilidades': '500+',
            'paises': '50+',
            'intercambios': '25,000+'
        }
    }
    
    return render(request, 'blog/acerca.html', context)

def login(request):
    """
    Vista para la página de inicio de sesión.
    Renderiza el template login.html
    """
    if request.method == 'POST':
        # Aquí iría la lógica de autenticación
        messages.success(request, '¡Bienvenido de vuelta!')
        return render(request, 'blog/login.html')
    
    return render(request, 'blog/login.html')

def registro(request):
    """
    Vista para la página de registro.
    Renderiza el template registro.html
    """
    if request.method == 'POST':
        # Aquí iría la lógica de registro
        messages.success(request, '¡Cuenta creada exitosamente!')
        return render(request, 'blog/registro.html')
    
    return render(request, 'blog/registro.html')

def dashboard(request):
    """
    Vista para el dashboard del usuario.
    Renderiza el template dashboard.html con datos dinámicos
    """
    # Datos de ejemplo para el dashboard
    context = {
        'usuario': {
            'nombre': 'Juan Pérez',
            'email': 'juan@ejemplo.com',
            'habilidades': ['Python', 'JavaScript', 'Diseño Web'],
            'puntuacion': 4.8
        },
        'estadisticas': {
            'intercambios_completados': 15,
            'habilidades_aprendidas': 8,
            'habilidades_enseñadas': 5,
            'horas_totales': 120
        },
        'actividad_reciente': [
            {'tipo': 'Intercambio completado', 'descripcion': 'Python por Guitarra', 'fecha': '2024-01-15'},
            {'tipo': 'Nueva habilidad', 'descripcion': 'React.js', 'fecha': '2024-01-10'},
            {'tipo': 'Evaluación recibida', 'descripcion': '5 estrellas', 'fecha': '2024-01-08'}
        ]
    }
    
    return render(request, 'blog/dashboard.html', context)