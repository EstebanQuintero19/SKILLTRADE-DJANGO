from django.db import models

# Create your models here.

class Intercambio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    aceptado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
