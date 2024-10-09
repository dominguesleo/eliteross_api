from django.contrib import admin
from models.models.user_models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'profession', 'fitness_goal')
    list_filter = ('gender', 'is_smoker', 'cigarette_per_day', 'physical_activity_at_work', 'is_physically_active', 'hours_of_sleep', 'is_active')
    search_fields = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'fitness_goal')
    ordering = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'profession', 'fitness_goal')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Health Information', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate', 'altered_analytical_data', 'disease', 'surgery', 'injury', 'contraindicated_physical_activity')}),
        ('Sports, rest, and nutrition', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'physical_activity', 'days_available_for_training', 'hours_of_sleep', 'daily_meals', 'allergies_intolerances')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
        ('Admin Information', {'fields': ('created_at', 'updated_at', 'is_active')}),
    )
    add_fieldsets = (
        ('Personal Information', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'gender', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Health Information', {'fields': ('is_smoker', 'cigarette_per_day', 'cholesterol', 'blood_pressure', 'heart_rate', 'altered_analytical_data', 'disease', 'surgery', 'injury', 'contraindicated_physical_activity')}),
        ('Sports, rest, and nutrition', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'physical_activity', 'days_available_for_training', 'hours_of_sleep', 'daily_meals', 'allergies_intolerances')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
    )


