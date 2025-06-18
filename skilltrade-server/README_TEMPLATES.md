# Sistema de Plantillas Django - SkillTrade

## 📋 Descripción General

Este proyecto implementa un sistema completo de plantillas en Django que demuestra las mejores prácticas para renderizar múltiples vistas y plantillas, estructurando correctamente rutas, vistas y archivos HTML.

## 🏗️ Estructura del Proyecto

```
skilltrade-server/
├── blog/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html          # Plantilla base principal
│   │       ├── index.html         # Página de inicio
│   │       ├── servicios.html     # Página de servicios
│   │       ├── acerca.html        # Página "Acerca de"
│   │       ├── contacto.html      # Página de contacto
│   │       ├── galeria.html       # Galería de videos
│   │       ├── login.html         # Formulario de login
│   │       ├── registro.html      # Formulario de registro
│   │       └── dashboard.html     # Dashboard del usuario
│   ├── views.py                   # Vistas de la aplicación
│   └── urls.py                    # Configuración de URLs
└── SKILLTRADE_project/
    ├── settings.py                # Configuración del proyecto
    └── urls.py                    # URLs principales
```

## 🎨 Características del Sistema de Plantillas

### 1. **Plantilla Base (`base.html`)**
- **Herencia de templates**: Todas las plantillas heredan de `base.html`
- **Navegación consistente**: Menú de navegación uniforme en todas las páginas
- **Sistema de mensajes**: Integración con Django messages framework
- **Footer responsivo**: Pie de página con enlaces y redes sociales
- **Archivos estáticos**: Bootstrap 5, Font Awesome, CSS personalizado

### 2. **Sistema de Bloques**
```html
{% block title %}Título de la página{% endblock %}
{% block content %}Contenido principal{% endblock %}
{% block extra_css %}CSS adicional{% endblock %}
{% block extra_js %}JavaScript adicional{% endblock %}
```

### 3. **Vistas y Contexto Dinámico**
- **Vistas con contexto**: Datos dinámicos pasados desde las vistas
- **Múltiples tipos de contenido**: Listas, diccionarios, objetos complejos
- **Formularios**: Manejo de formularios con CSRF protection

## 📱 Páginas Implementadas

### 1. **Página de Inicio (`index.html`)**
- Hero section con llamadas a la acción
- Sección de características principales
- Categorías de habilidades populares
- Call-to-action final

### 2. **Página de Servicios (`servicios.html`)**
- Lista dinámica de servicios desde la vista
- Comparación de planes de precios
- Características de los servicios
- Información de contacto

### 3. **Página "Acerca de" (`acerca.html`)**
- Misión y visión de la empresa
- Valores corporativos
- Estadísticas dinámicas
- Información del equipo
- Historia de la empresa

### 4. **Página de Contacto (`contacto.html`)**
- Formulario de contacto completo
- Información de contacto
- Preguntas frecuentes
- Enlaces a redes sociales

### 5. **Galería de Videos (`galeria.html`)**
- Grid responsivo de videos
- Categorías de videos
- Información detallada de cada video
- Video destacado

### 6. **Formularios de Autenticación**
- **Login (`login.html`)**: Formulario de inicio de sesión
- **Registro (`registro.html`)**: Formulario de registro completo

### 7. **Dashboard (`dashboard.html`)**
- Estadísticas del usuario
- Perfil de usuario
- Actividad reciente
- Acciones rápidas

## 🔧 Configuración de URLs

```python
# blog/urls.py
urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeriavideos, name='galeriavideos'),
    path('servicios/', servicios, name='servicios'),
    path('acerca/', acerca, name='acerca'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),
]
```

## 🎯 Características Técnicas

### 1. **Responsive Design**
- Bootstrap 5 para diseño responsivo
- Grid system adaptativo
- Componentes móvil-first

### 2. **Iconografía**
- Font Awesome 6.4.0
- Iconos consistentes en toda la aplicación
- Mejora la experiencia visual

### 3. **CSS Personalizado**
- Variables CSS para colores consistentes
- Animaciones y transiciones
- Estilos personalizados para componentes

### 4. **JavaScript**
- Bootstrap JavaScript para componentes interactivos
- Dropdowns, modales, tooltips
- Sistema de bloques para JS adicional

## 📊 Datos Dinámicos

### Ejemplo de Vista con Contexto:
```python
def servicios(request):
    servicios_lista = [
        {
            'nombre': 'Intercambio de Habilidades',
            'descripcion': 'Conecta con personas...',
            'icono': 'fas fa-exchange-alt',
            'precio': 'Gratis'
        },
        # ... más servicios
    ]
    
    context = {
        'servicios': servicios_lista,
        'total_servicios': len(servicios_lista)
    }
    
    return render(request, 'blog/servicios.html', context)
```

### Uso en Plantillas:
```html
{% for servicio in servicios %}
<div class="col-lg-6 col-xl-3">
    <div class="card h-100 text-center">
        <div class="card-body p-4">
            <i class="{{ servicio.icono }} fa-3x text-primary mb-3"></i>
            <h5 class="card-title fw-bold">{{ servicio.nombre }}</h5>
            <p class="card-text text-muted">{{ servicio.descripcion }}</p>
            <span class="badge bg-success fs-6">{{ servicio.precio }}</span>
        </div>
    </div>
</div>
{% endfor %}
```

## 🚀 Cómo Ejecutar

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

2. **Ejecutar migraciones**:
```bash
python manage.py migrate
```

3. **Iniciar el servidor**:
```bash
python manage.py runserver
```

4. **Acceder a las páginas**:
- Inicio: `http://localhost:8000/`
- Servicios: `http://localhost:8000/servicios/`
- Acerca de: `http://localhost:8000/acerca/`
- Contacto: `http://localhost:8000/contacto/`
- Galería: `http://localhost:8000/galeria/`
- Login: `http://localhost:8000/login/`
- Registro: `http://localhost:8000/registro/`
- Dashboard: `http://localhost:8000/dashboard/`

## 📚 Conceptos Aprendidos

### 1. **Herencia de Plantillas**
- Uso de `{% extends %}` y `{% block %}`
- Reutilización de código HTML
- Mantenimiento consistente

### 2. **Sistema de URLs**
- Configuración de `urlpatterns`
- Uso de `app_name` para namespacing
- URLs con nombres para referencias dinámicas

### 3. **Vistas y Contexto**
- Pasaje de datos desde vistas a plantillas
- Uso de diccionarios y listas en contexto
- Renderizado dinámico de contenido

### 4. **Formularios**
- Manejo de formularios HTML
- Protección CSRF
- Validación de datos

### 5. **Diseño Responsivo**
- Uso de Bootstrap 5
- Grid system adaptativo
- Componentes móvil-first

## 🎨 Personalización

### Colores del Tema:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --light-bg: #ecf0f1;
    --dark-text: #2c3e50;
}
```

### Agregar Nuevas Páginas:
1. Crear la vista en `views.py`
2. Agregar la URL en `urls.py`
3. Crear la plantilla HTML
4. Heredar de `base.html`

## 📝 Notas Importantes

- Todas las plantillas heredan de `base.html`
- Se utiliza Bootstrap 5 para el diseño
- Los formularios incluyen protección CSRF
- El sistema es completamente responsivo
- Los datos son dinámicos desde las vistas
- Se incluyen iconos de Font Awesome

## 🔗 Enlaces Útiles

- [Documentación de Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Django URL Patterns](https://docs.djangoproject.com/en/5.2/topics/http/urls/)

---

**Desarrollado para el aprendizaje del sistema de plantillas de Django** 