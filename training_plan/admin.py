from django.contrib import admin
from .models import *

class MacronutrientInline(admin.TabularInline):
    model = Macronutrient
    extra = 0

class TrainingDayInline(admin.TabularInline):
    model = TrainingDay
    extra = 0
    filter_horizontal = ('warm_up', 'exercises')

@admin.register(Mesocycle)
class MesocycleAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('client', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('client__name', 'client__last_name', 'name', 'start_date', 'end_date', 'description')
    ordering = ('client', 'name', 'start_date', 'end_date', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    fieldsets = (
        ('Información Personal', {'fields': ('client', 'name', 'start_date', 'end_date', 'description')}),
        ('Información de administración', {'fields': ('created_at', 'updated_at')}),
    )
    inlines = [MacronutrientInline, TrainingDayInline]

@admin.register(Macronutrient)
class MacronutrientAdmin(admin.ModelAdmin):
    list_display = ('mesocycle', 'calories', 'protein', 'carbs', 'fats', 'created_at', 'updated_at')
    list_filter = ('mesocycle', 'calories', 'protein', 'carbs', 'fats', 'created_at', 'updated_at')
    search_fields = ('mesocycle__name','mesocycle__client__name', 'mesocycle__client__last_name', 'calories', 'protein', 'carbs', 'fats', 'description')
    ordering = ('mesocycle', 'calories', 'protein', 'carbs', 'fats', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    fieldsets = (
        ('Información Personal', {'fields': ('mesocycle', 'calories', 'protein', 'carbs', 'fats', 'description')}),
        ('Información de administración', {'fields': ('created_at', 'updated_at')}),
    )

@admin.register(TrainingDay)
class TrainingDayAdmin(admin.ModelAdmin):
    list_display = ('mesocycle', 'day', 'title', 'created_at', 'updated_at')
    list_filter = ('mesocycle', 'day', 'title', 'created_at', 'updated_at')
    search_fields = ('mesocycle__name', 'mesocycle__client__name', 'mesocycle__client__last_name', 'day', 'title', 'description')
    ordering = ('mesocycle', 'day', 'title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    fieldsets = (
        ('Información Personal', {'fields': ('mesocycle', 'day', 'title', 'description', 'warm_up', 'exercises')}),
        ('Información de administración', {'fields': ('created_at', 'updated_at')}),
    )
    filter_horizontal = ('warm_up', 'exercises')

