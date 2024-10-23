from django.contrib import admin
from models.models.user_models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'profession', 'fitness_goal')
    list_filter = ('gender', 'is_smoker', 'cigarette_per_day', 'physical_activity_at_work', 'is_physically_active', 'hours_of_sleep', 'is_active')
    search_fields = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'fitness_goal')
    ordering = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'profession', 'fitness_goal')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Personal', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Información de Salud', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate')}),
        ('Deporte, descanso y nutrición', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'days_available_for_training', 'hours_of_sleep')}),
        ('Pruebas y mediciones', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
        ('Información de administración', {'fields': ('created_at', 'updated_at', 'is_active')}),
    )
    add_fieldsets = (
        ('Información Persona', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Información de Salud', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate')}),
        ('Deporte, descanso y nutrición', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'days_available_for_training', 'hours_of_sleep')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
    )

@admin.register(AlteredAnalyticalData)
class AlteredAnalyticalDataAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'details')
    search_fields = ('client__name', 'client__last_name', 'details')
    ordering = ('client', 'name', 'details')
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
    fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )
    add_fieldsets = (
        (None, {'fields': ('client', 'name', 'details')}),
    )