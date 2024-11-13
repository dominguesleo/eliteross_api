from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(null=True, blank=True, default=None, verbose_name="Descripción")
    image = models.ImageField(null=True, blank=True,  default=None, upload_to='exercises', verbose_name="Imagen")
    video_url = models.URLField(null=True, blank=True, default=None, verbose_name="URL Video")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
