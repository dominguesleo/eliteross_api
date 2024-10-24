from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from models.models.user_models import *
from models.models.body_measurement_models import *

#* inlines

class AlteredAnalyticalDataInline(admin.TabularInline):
    model = AlteredAnalyticalData
    extra = 0

class DiseaseInline(admin.TabularInline):
    model = Disease
    extra = 0

class SurgeryInline(admin.TabularInline):
    model = Surgery
    extra = 0

class InjuryInline(admin.TabularInline):
    model = Injury
    extra = 0

class ContraindicatedPhysicalActivityInline(admin.TabularInline):
    model = ContraindicatedPhysicalActivity
    extra = 0

class PhysicalActivityInline(admin.TabularInline):
    model = PhysicalActivity
    extra = 0

class DailyMealsInline(admin.TabularInline):
    model = DailyMeals
    extra = 0

class AllergiesIntolerancesInline(admin.TabularInline):
    model = AllergiesIntolerances
    extra = 0

class SupplementsInline(admin.TabularInline):
    model = Supplements
    extra = 0

#* user_models

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'fitness_goal', 'view_body_measurements_link')
    list_filter = ('gender', 'is_smoker', 'cigarette_per_day', 'physical_activity_at_work', 'is_physically_active', 'hours_of_sleep', 'is_active')
    search_fields = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'fitness_goal')
    ordering = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'profession', 'fitness_goal')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    fieldsets = (
        ('Información Personal', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'height', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Información de Salud', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate')}),
        ('Deporte, descanso y nutrición', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'days_available_for_training', 'hours_of_sleep')}),
        ('Pruebas y mediciones', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
        ('Información de administración', {'fields': ('created_at', 'updated_at', 'is_active')}),
    )
    add_fieldsets = (
        ('Información Persona', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'height', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Información de Salud', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate')}),
        ('Deporte, descanso y nutrición', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'days_available_for_training', 'hours_of_sleep')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
    )
    inlines = [AlteredAnalyticalDataInline, DiseaseInline, SurgeryInline, InjuryInline, ContraindicatedPhysicalActivityInline, PhysicalActivityInline, DailyMealsInline, AllergiesIntolerancesInline, SupplementsInline]

    @admin.display(description='Medidas Corporales')
    def view_body_measurements_link(self, obj):
        url = reverse('admin:models_bodymeasurement_changelist') + f'?client__id__exact={obj.id}'
        return format_html('<a href="{}">Medidas Corporales</a>', url)

@admin.register(AlteredAnalyticalData)
class AlteredAnalyticalDataAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(ContraindicatedPhysicalActivity)
class ContraindicatedPhysicalActivityAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(PhysicalActivity)
class PhysicalActivityAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'per_week', 'level', 'details')
    list_filter = ('per_week', 'level')
    search_fields = ('client__name', 'client__last_name','per_week', 'level', 'details')
    ordering = ('client', 'name', 'per_week', 'level', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'per_week', 'level', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'per_week', 'level', 'details')}),
    )

@admin.register(DailyMeals)
class DailyMealsAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(AllergiesIntolerances)
class AllergiesIntolerancesAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

@admin.register(Supplements)
class SupplementsAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
    save_on_top = True
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )

#* body_measurement_models

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