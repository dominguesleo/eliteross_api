from django.db import models
from user.models import Client
from exercise.models import Exercise

DAYS_CHOICES = (
    ('Monday', 'Lunes'),
    ('Tuesday', 'Martes'),
    ('Wednesday', 'Miércoles'),
    ('Thursday', 'Jueves'),
    ('Friday', 'Viernes'),
    ('Saturday', 'Sábado'),
    ('Sunday', 'Domingo'),
)

class Mesocycle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='mesocycle', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    start_date = models.DateField(null=True, blank=True, default=None, verbose_name="Fecha de inicio")
    end_date = models.DateField(null=True, blank=True, default=None, verbose_name="Fecha de finalización")
    description = models.TextField(null=True, blank=True, default=None, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Mesociclo"
        verbose_name_plural = "Mesociclos"

class Macronutrient(models.Model):
    mesocycle = models.ForeignKey(Mesocycle, on_delete=models.CASCADE, related_name='macronutrient', verbose_name="Mesociclo")
    calories = models.FloatField(verbose_name="Calorías (kcal)")
    protein = models.FloatField(verbose_name="Proteínas (g)")
    carbs = models.FloatField(verbose_name="Carbohidratos (g)")
    fats = models.FloatField(verbose_name="Grasas (g)")
    description = models.TextField(null=True, blank=True, default=None, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.mesocycle.name} - Macronutrientes"

    class Meta:
        verbose_name = "Macronutriente"
        verbose_name_plural = "Macronutrientes"

class TrainingDay(models.Model):
    mesocycle = models.ForeignKey(Mesocycle, on_delete=models.CASCADE, related_name='training_day', verbose_name="Mesociclo")
    day = models.CharField(max_length=10, choices=DAYS_CHOICES, verbose_name="Día")
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(null=True, blank=True, default=None, verbose_name="Descripción")
    warm_up = models.ManyToManyField(Exercise, related_name='training_day_warm_up', verbose_name="Calentamiento")
    exercises = models.ManyToManyField(Exercise, related_name='training_day_exercises', verbose_name="Ejercicios")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.mesocycle.client.name} {self.mesocycle.client.last_name} - {self.day}"

    class Meta:
        verbose_name = "Día de entrenamiento"
        verbose_name_plural = "Días de entrenamiento"