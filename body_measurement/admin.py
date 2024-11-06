from django.contrib import admin
from .models import *

@admin.register(BodyMeasurement)
class BodyMeasurementAdmin(admin.ModelAdmin):
    list_display = ('client', 'date')
    search_fields = ('client__name', 'client__last_name', 'date')
    ordering = ('client', 'date')
    save_on_top = True
    readonly_fields = ('central_adiposity_index', 'peripheral_adiposity_index', 'imc', 'rcq', 'ic', 'waist_height_ratio', 'pollock_3', 'pollock_7', 'petroski', 'faulkner', 'sloan', 'guedes', 'jackson_pollock', 'weltman', 'navy_body_fat', 'ymca', 'deurenberg')
    fieldsets = (
        ('General', {'fields': ('client', 'date', 'weight')}),
        ('Circunferencias', {'fields': ('chest_circ', 'right_arm_circ', 'left_arm_circ', 'right_forearm_circ', 'left_forearm_circ', 'abdomen_circ', 'waist_circ', 'hip_circ', 'right_thigh_circ', 'left_thigh_circ', 'right_calf_circ', 'left_calf_circ')}),
        ('Pliegues cutáneos', {'fields': ('neck_circ', 'chest_skf', 'mid_axillary_skf', 'subscapular_skf', 'triceps_skf', 'biceps_skf', 'suprailiac_skf', 'abdomen_skf', 'thigh_skf', 'calf_skf')}),
        ('Campos calculados', {'fields': ('central_adiposity_index', 'peripheral_adiposity_index', 'imc', 'rcq', 'ic', 'waist_height_ratio', 'pollock_3', 'pollock_7', 'petroski', 'faulkner', 'sloan', 'guedes', 'jackson_pollock', 'weltman', 'navy_body_fat', 'ymca', 'deurenberg')}),
    )
    add_fieldsets = (
        ('General', {'fields': ('client', 'date', 'weight')}),
        ('Circunferencias', {'fields': ('chest_circ', 'right_arm_circ', 'left_arm_circ', 'right_forearm_circ', 'left_forearm_circ', 'abdomen_circ', 'waist_circ', 'hip_circ', 'right_thigh_circ', 'left_thigh_circ', 'right_calf_circ', 'left_calf_circ')}),
        ('Pliegues cutáneos', {'fields': ('neck_circ', 'chest_skf', 'mid_axillary_skf', 'subscapular_skf', 'triceps_skf', 'biceps_skf', 'suprailiac_skf', 'abdomen_skf', 'thigh_skf', 'calf_skf')}),
    )