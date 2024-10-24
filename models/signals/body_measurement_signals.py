from django.db.models.signals import pre_save
from django.dispatch import receiver
from models.models.body_measurement_models import BodyMeasurement
from models.utils.body_measurement_utils import *

@receiver(pre_save, sender=BodyMeasurement)
def calculate_body_measurement(sender, instance, **kwargs):
    instance.central_adiposity_index = central_adiposity_index(instance.subscapular_skf, instance.suprailiac_skf)
    instance.peripheral_adiposity_index = peripheral_adiposity_index(instance.triceps_skf, instance.biceps_skf)
    instance.imc = imc(instance.weight, instance.client.height)
    instance.rcq = rcq(instance.waist_circ, instance.hip_circ)
    instance.ic = ic(instance.waist_circ, instance.weight, instance.client.height)
    instance.waist_height_ratio = waist_height_ratio(instance.waist_circ, instance.client.height)
    instance.pollock_3 = siri(pollock_3(instance.client.gender, instance.client.age, instance.chest_skf, instance.abdomen_skf, instance.triceps_skf, instance.suprailiac_skf, instance.thigh_skf))
    instance.pollock_7 = siri(pollock_7(instance.client.gender, instance.client.age, instance.chest_skf, instance.mid_axillary_skf, instance.subscapular_skf, instance.triceps_skf, instance.abdomen_skf, instance.thigh_skf, instance.suprailiac_skf))
    instance.petroski = siri(petroski(instance.client.gender, instance.client.age, instance.triceps_skf, instance.subscapular_skf, instance.suprailiac_skf, instance.calf_skf))
    instance.faulkner = faulkner(instance.client.gender, instance.triceps_skf, instance.subscapular_skf, instance.suprailiac_skf, instance.abdomen_skf)
    instance.sloan = siri(sloan(instance.client.gender, instance.subscapular_skf, instance.thigh_skf,instance.triceps_skf, instance.suprailiac_skf))
    instance.guedes = siri(guedes(instance.client.gender, instance.triceps_skf, instance.abdomen_skf, instance.suprailiac_skf, instance.thigh_skf, instance.subscapular_skf))
    instance.jackson_pollock = siri(jackson_pollock(instance.client.gender, instance.client.age, instance.chest_skf, instance.abdomen_skf, instance.thigh_skf, instance.mid_axillary_skf, instance.triceps_skf, instance.suprailiac_skf, instance.subscapular_skf))
    instance.weltman = weltman(instance.client.gender, instance.abdomen_circ, instance.weight, instance.client.height)
    instance.navy_body_fat = navy_body_fat(instance.client.gender, instance.client.height, instance.waist_circ, instance.neck_circ,instance.hip_circ)
    instance.ymca = ymca(instance.client.gender, instance.weight, instance.waist_circ)
    instance.deurenberg = deurenberg(instance.client.gender, instance.client.age, instance.weight, instance.client.height)

    print(instance.client.height)

