from django.apps import AppConfig


class BusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bus'

    def ready(self):
        import Bus.signals  # Importa las señales cuando la app esté lista
