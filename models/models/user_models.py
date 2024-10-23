from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

GENDER_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
]

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

FLEXIBILITY_CHOICES = [
    ('Good', 'Good'),
    ('Regular', 'Regular'),
    ('Bad', 'Bad'),
]

class Client(models.Model):

    # Personal Information
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    date_of_birth = models.DateField(verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    email = models.EmailField(null=True, blank=True, verbose_name="Correo electrónico")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name="Género")
    height = models.FloatField(null=True, blank=True, verbose_name="Altura")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Dirección")
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name="Profesión")
    physical_activity_at_work = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None, verbose_name="Actividad física en el trabajo")
    fitness_goal = models.CharField(max_length=100, null=True, blank=True, verbose_name="Objetivo de fitness")

    # Health Information
    is_smoker = models.BooleanField(null=True, default=None, verbose_name="¿Fumador?")
    cigarette_per_day = models.CharField(max_length=100, null=True, blank=True, choices=CIGARETTE_CHOICES, default=None, verbose_name="Cigarrillos por día")
    cholesterol = models.FloatField(null=True, blank=True, verbose_name="Colesterol")
    blood_pressure = models.FloatField(null=True, blank=True, verbose_name="Presión arterial")
    heart_rate = models.FloatField(null=True, blank=True, verbose_name="Frecuencia cardíaca")

    # Sports, rest, and nutrition
    is_physically_active = models.BooleanField(null=True, default=None, verbose_name="¿Activo físicamente?")
    physical_inactivity_per_month = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True, verbose_name="Inactividad física por mes")
    days_available_for_training = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)], null=True, blank=True, verbose_name="Días disponibles para entrenar")
    hours_of_sleep = models.CharField(max_length=100, null=True, blank=True, choices=SLEEP_CHOICES, default=None, verbose_name="Horas de sueño")

    # Tests and measurements
    biotype = models.CharField(max_length=100, null=True, blank=True, verbose_name="Biotipo")
    shoulder_flexibility = models.CharField(null=True, blank=True, choices=FLEXIBILITY_CHOICES, default=None, verbose_name="Flexibilidad de hombros")
    hip_flexibility = models.CharField(null=True, blank=True, choices=FLEXIBILITY_CHOICES, default=None, verbose_name="Flexibilidad de cadera")
    knee_flexibility = models.CharField(null=True, blank=True, choices=FLEXIBILITY_CHOICES, default=None, verbose_name="Flexibilidad de rodilla")
    ankle_flexibility = models.CharField(null=True, blank=True, choices=FLEXIBILITY_CHOICES, default=None, verbose_name="Flexibilidad de tobillo")

    # Admin Information
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


#* Health Information relationships

class AlteredAnalyticalData(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='altered_analytical_data', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Dato Analítico Alterado"
        verbose_name_plural = "Datos Analíticos Alterados"

class Disease(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='disease', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Enfermedad"
        verbose_name_plural = "Enfermedades"

class Surgery(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='surgery', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Cirugía"
        verbose_name_plural = "Cirugías"

class Injury(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='injury', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Lesión"
        verbose_name_plural = "Lesiones"

class ContraindicatedPhysicalActivity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contraindicated_physical_activity', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Actividad Física Contraindicada"
        verbose_name_plural = "Actividades Físicas Contraindicadas"


#* Sports, rest, and nutrition relationships

class PhysicalActivity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='physical_activity', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    per_week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], null=True, blank=True, verbose_name="Por semana")
    level = models.CharField(max_length=100, null=True, blank=True, choices=PHYSICAL_ACTIVITY_CHOICES, default=None, verbose_name="Nivel")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Actividad Física"
        verbose_name_plural = "Actividades Físicas"

class DailyMeals(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='daily_meals', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Comida Diaria"
        verbose_name_plural = "Comidas Diarias"

class AllergiesIntolerances(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='allergies_intolerances', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Alergia o Intolerancia"
        verbose_name_plural = "Alergias e Intolerancias"

class Supplements(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='supplements', verbose_name="Cliente")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    details = models.TextField(null=True, blank=True, verbose_name="Detalles")

    def __str__(self):
        return f"{self.client.name} {self.client.last_name} - {self.name}"

    class Meta:
        verbose_name = "Suplemento"
        verbose_name_plural = "Suplementos"
