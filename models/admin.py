from django.contrib import admin
from models.models.user_models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'profession', 'fitness_goal')
    list_filter = ('is_smoker', 'cigarette_per_day', 'is_diabetic', 'diabetic_type', 'physical_activity_at_work', 'is_physically_active', 'level_of_physical_activity', 'hours_of_sleep', 'is_active')
    search_fields = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'fitness_goal')
    ordering = ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'profession', 'fitness_goal')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Health Information', {'fields': ('is_smoker', 'cigarette_per_day', 'is_diabetic', 'diabetic_type', 'cholesterol', 'blood_pressure', 'heart_rate', 'altered_analytical_data', 'diseases', 'surgeries', 'injuries', 'contraindicated_physical_activity')}),
        ('Sports, rest, and nutrition', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'physical_activity', 'physical_activity_per_week', 'level_of_physical_activity', 'days_available_for_training', 'hours_of_sleep', 'daily_meals', 'allergies_intolerances')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
        ('Admin Information', {'fields': ('created_at', 'updated_at', 'is_active')}),
    )
    add_fieldsets = (
        ('Personal Information', {'fields': ('name', 'last_name', 'date_of_birth', 'phone', 'email', 'address', 'profession', 'physical_activity_at_work', 'fitness_goal')}),
        ('Health Information', {'fields': ('is_smoker', 'cigarette_per_day', 'is_diabetic', 'diabetic_type', 'cholesterol', 'blood_pressure', 'heart_rate', 'altered_analytical_data', 'diseases', 'surgeries', 'injuries', 'contraindicated_physical_activity')}),
        ('Sports, rest, and nutrition', {'fields': ('is_physically_active', 'physical_inactivity_per_month', 'physical_activity', 'physical_activity_per_week', 'level_of_physical_activity', 'days_available_for_training', 'hours_of_sleep', 'daily_meals', 'allergies_intolerances')}),
        ('Tests and measurements', {'fields': ('biotype', 'shoulder_flexibility', 'hip_flexibility', 'knee_flexibility', 'ankle_flexibility')}),
    )


