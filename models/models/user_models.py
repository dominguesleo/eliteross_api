from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):

    PHYSICAL_ACTIVITY_CHOICES = [
        ('Sedentary', 'Sedentary'),
        ('Lightly Sedentary'),
        ('Light', 'Light'),
        ('Moderate', 'Moderate'),
        ('Intense', 'Intense'),
    ]

    CIGARETTE_CHOICES = [
        ('1-5', '1-5'),
        ('6-20', '6-20'),
        ('+20', '+20'),
    ]

    DIABETIC_CHOICES = [
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
    ]

    SLEEP_CHOICES = [
        ('-6 hours', '-6 hours'),
        ('6-7 hours', '6-7 hours'),
        ('8 hours', '8 hours'),
        ('+9 hours', '+9 hours'),
    ]

    MEALS_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Mid-morning snack', 'Mid-morning snack'),
        ('Lunch', 'Lunch'),
        ('Mid-Afternoon snack', 'Mid-Afternoon snack'),
        ('Dinner', 'Dinner'),
        ('Evening snack', 'Evening snack'),
        ('Others', 'Others'),
    ]

    # Personal Information
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    physical_activity_at_work = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None)
    fitness_goal = models.CharField(max_length=100)

    # Health Information
    is_smoker = models.BooleanField()
    cigarette_per_day =  models.CharField(max_length=100, null=True, blank=True, choices=CIGARETTE_CHOICES, default=None)
    is_diabetic = models.BooleanField()
    diabetic_type = models.CharField(max_length=100, null=True, blank=True, choices=DIABETIC_CHOICES, default=None)
    cholesterol = models.FloatField()
    blood_pressure = models.FloatField()
    heart_rate = models.FloatField()
    altered_analytical_data = ArrayField(models.CharField(max_length=200),blank=True, default=list)
    diseases = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    surgeries = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    injuries = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    contraindicated_physical_activity = ArrayField(models.CharField(max_length=200),blank=True, default=list)

    # Sports, rest, and nutrition
    is_physically_active = models.BooleanField()
    physical_inactivity_per_month = models.IntegerField()
    physical_activity =ArrayField(models.CharField(max_length=200), blank=True, default=list)
    physical_activity_per_week = models.IntegerField()
    level_of_physical_activity = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None)
    days_available_for_training = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    hours_of_sleep = models.CharField(max_length=100, null=True, blank=True, choices=SLEEP_CHOICES, default=None)
    daily_meals = ArrayField(models.CharField(max_length=200, choices=MEALS_CHOICES), blank=True, default=list)
    allergies_intolerances = ArrayField(models.CharField(max_length=200), blank=True, default=list)













