from django.db import models
from models.models.user_models import Client

class BodyMeasurement(models.Model):

# General
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='body_measurement', verbose_name="Cliente")
    date = models.DateField(verbose_name="Fecha")

    # Circunferences
    chest_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del pecho")
    right_arm_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del brazo derecho")
    left_arm_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del brazo izquierdo")
    right_forearm_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del antebrazo derecho")
    left_forearm_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del antebrazo izquierdo")
    abdomen_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del abdomen")
    waist_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia de la cintura")
    hip_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia de la cadera")
    right_thigh_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del muslo derecho")
    left_thigh_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia del muslo izquierdo")
    right_calf_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia de la pantorrilla derecha")
    left_calf_circ = models.FloatField(null=True, blank=True, verbose_name="Circunferencia de la pantorrilla izquierda")

    # Skinfolds
    chest_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del pecho")
    mid_axillary_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo axilar medio")
    subscapular_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo subescapular")
    triceps_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del tríceps")
    biceps_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del bíceps")
    suprailiac_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo suprailiaco")
    abdomen_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del abdomen")
    thigh_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del muslo")
    calf_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo de la pantorrilla")

    class Meta:
        verbose_name = "Medición Corporal"
        verbose_name_plural = "Mediciones Corporales"
