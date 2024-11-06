from django.apps import AppConfig

class BodyMeasurementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'body_measurement'
    verbose_name = 'Medición Corporal'

    def ready(self):
        import body_measurement.signals
