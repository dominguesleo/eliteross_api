from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")
    image = models.ImageField(upload_to='exercises', null=True, blank=True, verbose_name="Imagen")
    video_url = models.URLField(null=True, blank=True, verbose_name="URL Video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
