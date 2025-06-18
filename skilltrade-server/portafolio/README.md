# App Portafolio - SkillTrade Server

## Descripción

La aplicación `portafolio` es un sistema completo de portafolio personal para desarrolladores web, construido con Django y Bootstrap. Incluye tres vistas principales con plantillas modernas y responsivas.



### 📱 Vistas Disponibles

#### 1. **Inicio** (`/portafolio/`)
- **Hero Section**: Presentación personal con llamadas a la acción
- **Sobre Mí**: Información personal y experiencia
- **Habilidades**: Lista dinámica de tecnologías y herramientas
- **Estadísticas**: Contadores animados de experiencia y proyectos
- **Call-to-Action**: Enlaces a proyectos y contacto

#### 2. **Proyectos** (`/portafolio/proyectos/`)
- **Grid de Proyectos**: Muestra dinámica de proyectos con detalles
- **Categorías**: E-commerce, Aplicaciones Web, Sitios Web
- **Proceso de Desarrollo**: Metodología de trabajo explicada
- **Enlaces**: Código fuente y demos de cada proyecto

#### 3. **Contacto** (`/portafolio/contacto/`)
- **Información de Contacto**: Email, teléfono, ubicación
- **Formulario de Contacto**: Con validación y envío
- **Redes Sociales**: Enlaces a perfiles profesionales
- **FAQ**: Preguntas frecuentes sobre servicios
- **Disponibilidad**: Estado actual de disponibilidad

### 🎯 Funcionalidades Técnicas

#### CSS Personalizado
- **Variables CSS**: Sistema de colores consistente
- **Animaciones**: Efectos de entrada y hover
- **Glassmorphism**: Efectos de cristal modernos
- **Responsive Design**: Adaptación a todos los dispositivos

#### JavaScript Interactivo
- **Animaciones de Scroll**: Efectos al hacer scroll
- **Contadores Animados**: Estadísticas con animación
- **Validación de Formularios**: Validación en tiempo real
- **Efectos de Partículas**: Animaciones en el hero section
- **Smooth Scrolling**: Navegación suave entre secciones

## Estructura de Archivos

```
portafolio/
├── templates/
│   └── portafolio/
│       ├── base.html          # Plantilla base con navegación
│       ├── inicio.html        # Página de inicio
│       ├── proyectos.html     # Página de proyectos
│       └── contacto.html      # Página de contacto
├── static/
│   └── portafolio/
│       ├── css/
│       │   └── style.css      # Estilos personalizados
│       └── js/
│           └── script.js      # JavaScript personalizado
├── views.py                   # Vistas de la aplicación
├── urls.py                    # Configuración de URLs
└── README.md                  # Este archivo
```

## Configuración

### 1. Instalación
La app ya está configurada en `INSTALLED_APPS` del proyecto principal.

### 2. URLs
Las URLs están configuradas en:
- **App URLs**: `portafolio/urls.py`
- **Proyecto URLs**: `SKILLTRADE_project/urls.py`

### 3. Vistas
Las vistas están definidas en `views.py` con contexto dinámico:

```python
# Ejemplo de contexto para la vista de inicio
context = {
    'nombre': 'Juan Pérez',
    'titulo': 'Desarrollador Full Stack',
    'descripcion': 'Apasionado por crear soluciones web innovadoras...',
    'experiencia': '2 años',
    'proyectos_completados': 25,
    'habilidades': ['Python', 'Django', 'JavaScript', 'React', 'Bootstrap']
}
```

## Personalización

### Colores
Los colores se pueden personalizar en las variables CSS:

```css
:root {
    --primary-color: #2d3436;    /* Color principal */
    --secondary-color: #0984e3;  /* Color secundario */
    --accent-color: #00b894;     /* Color de acento */
    --text-color: #2d3436;       /* Color de texto */
    --light-bg: #f8f9fa;         /* Fondo claro */
    --dark-bg: #2d3436;          /* Fondo oscuro */
}
```

### Contenido
El contenido se puede personalizar modificando el contexto en las vistas:

1. **Información Personal**: Nombre, título, descripción
2. **Proyectos**: Lista de proyectos con detalles
3. **Habilidades**: Tecnologías y herramientas
4. **Contacto**: Información de contacto y redes sociales

### Estilos
Los estilos se pueden personalizar en:
- `static/portafolio/css/style.css` - Estilos adicionales
- Plantillas HTML - Estilos inline para ajustes específicos

## Características Avanzadas

### 🎨 Efectos Visuales
- **Hover Effects**: Animaciones al pasar el mouse
- **Scroll Animations**: Efectos al hacer scroll
- **Particle Effects**: Partículas animadas en el hero
- **Gradient Backgrounds**: Fondos con gradientes modernos

### 📱 Responsive Design
- **Mobile First**: Diseño optimizado para móviles
- **Breakpoints**: Adaptación a tablets y desktop
- **Flexible Grid**: Sistema de grid responsivo
- **Touch Friendly**: Optimizado para dispositivos táctiles

### ⚡ Performance
- **Lazy Loading**: Carga diferida de imágenes
- **Optimized CSS**: Estilos optimizados
- **Minified JS**: JavaScript comprimido
- **CDN Resources**: Recursos externos optimizados

## Uso

### Acceso a las Páginas
1. **Inicio**: `http://localhost:8000/portafolio/`
2. **Proyectos**: `http://localhost:8000/portafolio/proyectos/`
3. **Contacto**: `http://localhost:8000/portafolio/contacto/`

### Navegación
- **Menú Principal**: Navegación fija en la parte superior
- **Enlaces Internos**: Navegación suave entre secciones
- **Call-to-Actions**: Botones de acción en cada página


### Agregar Nuevas Funcionalidades
1. **Nuevas vistas**: Agregar en `views.py`
2. **Nuevas URLs**: Configurar en `urls.py`
3. **Nuevas plantillas**: Crear archivos HTML
4. **Nuevos estilos**: Agregar CSS/JS según sea necesario

