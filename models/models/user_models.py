from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Client(models.Model):

    PHYSICAL_ACTIVITY_CHOICES = [
        ('Sedentary', 'Sedentary'),
        ('Lightly Sedentary', 'Lightly Sedentary'),
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
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    physical_activity_at_work = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None)
    fitness_goal = models.CharField(max_length=100, null=True, blank=True)

    # Health Information
    is_smoker = models.BooleanField(null=True)
    cigarette_per_day =  models.CharField(max_length=100, null=True, blank=True, choices=CIGARETTE_CHOICES, default=None)
    is_diabetic = models.BooleanField(null=True)
    diabetic_type = models.CharField(max_length=100, null=True, blank=True, choices=DIABETIC_CHOICES, default=None)
    cholesterol = models.FloatField(null=True, blank=True)
    blood_pressure = models.FloatField(null=True, blank=True)
    heart_rate = models.FloatField(null=True, blank=True)
    altered_analytical_data = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    diseases = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    surgeries = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    injuries = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    contraindicated_physical_activity = ArrayField(models.CharField(max_length=200), blank=True, default=list)

    # Sports, rest, and nutrition
    is_physically_active = models.BooleanField(null=True)
    physical_inactivity_per_month = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    physical_activity =ArrayField(models.CharField(max_length=200), blank=True, default=list)
    physical_activity_per_week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], null=True, blank=True)
    level_of_physical_activity = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None)
    days_available_for_training = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], null=True, blank=True)
    hours_of_sleep = models.CharField(max_length=100, null=True, blank=True, choices=SLEEP_CHOICES, default=None)
    daily_meals = ArrayField(models.CharField(max_length=200, choices=MEALS_CHOICES), blank=True, default=list)
    allergies_intolerances = ArrayField(models.CharField(max_length=200), blank=True, default=list)

    # Tests and measurements
    biotype = models.CharField(max_length=100, null=True, blank=True)
    shoulder_flexibility = models.FloatField(null=True, blank=True)
    hip_flexibility = models.FloatField(null=True, blank=True)
    knee_flexibility = models.FloatField(null=True, blank=True)
    ankle_flexibility = models.FloatField(null=True, blank=True)

    # Admin Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def __str__(self):
        return f'{self.name} {self.last_name}'

class WeightRecord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='weight_records')
    weight = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.weight} kg at {self.recorded_at}"

class HeightRecord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='height_records')
    height = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.height} cm at {self.recorded_at}"

class WaistRecord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='waist_records')
    waist = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.waist} cm at {self.recorded_at}"












