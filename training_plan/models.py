from django.db import models
from user.models import Client

class Mesocycle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='mesocycle', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de finalización")
    goal = models.CharField(max_length=100, verbose_name="Objetivo")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Mesociclo"
        verbose_name_plural = "Mesociclos"
    

