from django.db import models
from models.models.user_models import Client

class BodyMeasurement(models.Model):

    # General
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='body_measurement', verbose_name="Cliente")
    date = models.DateField(verbose_name="Fecha")
    weight = models.FloatField(null=True,blank=True, default=None, verbose_name="Peso")

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
    neck_circ = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del cuello")
    chest_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del pecho")
    mid_axillary_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo axilar medio")
    subscapular_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo subescapular")
    triceps_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del tríceps")
    biceps_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del bíceps")
    suprailiac_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo suprailiaco")
    abdomen_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del abdomen")
    thigh_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo del muslo")
    calf_skf = models.FloatField(null=True, blank=True, verbose_name="Pliegue cutáneo de la pantorrilla")

    # Calculated fields
    central_adiposity_index = models.FloatField(null=True, blank=True, default=None, verbose_name="Índice de adiposidad central")
    peripheral_adiposity_index = models.FloatField(null=True, blank=True, default=None, verbose_name="Índice de adiposidad periférica")
    imc = models.FloatField(null=True, blank=True, default=None, verbose_name="IMC")
    rcq = models.FloatField(null=True, blank=True, default=None, verbose_name="RCQ")
    ic = models.FloatField(null=True, blank=True, default=None, verbose_name="IC")
    waist_height_ratio = models.FloatField(null=True, blank=True, default=None, verbose_name="Relación cintura altura")
    pollock_3 = models.FloatField(null=True, blank=True, default=None, verbose_name="Pollock 3")
    pollock_7 = models.FloatField(null=True, blank=True, default=None, verbose_name="Pollock 7")
    petroski = models.FloatField(null=True, blank=True, default=None, verbose_name="Petroski")
    faulkner = models.FloatField(null=True, blank=True, default=None, verbose_name="Faulkner")
    sloan = models.FloatField(null=True, blank=True, default=None, verbose_name="Sloan")
    guedes = models.FloatField(null=True, blank=True, default=None, verbose_name="Guedes")
    jackson_pollock = models.FloatField(null=True, blank=True, default=None, verbose_name="Jackson & Pollock")
    weltman = models.FloatField(null=True, blank=True, default=None, verbose_name="Weltman")
    navy_body_fat = models.FloatField(null=True, blank=True, default=None, verbose_name="Formula marina EEUU")
    ymca = models.FloatField(null=True, blank=True, default=None, verbose_name="YMCA")
    deurenberg = models.FloatField(null=True, blank=True, default=None, verbose_name="Deurenberg")

    class Meta:
        verbose_name = "Medición Corporal"
        verbose_name_plural = "Mediciones Corporales"
