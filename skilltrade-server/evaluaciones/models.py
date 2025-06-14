from django.db import models

# Create your models here.

class Evaluacion(models.Model):
    titulo = models.CharField(max_length=200)
    comentario = models.TextField(blank=True, null=True)
    puntuacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
