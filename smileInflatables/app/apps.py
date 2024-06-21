from django.apps import AppConfig as renamedConfig

class AppConfig(renamedConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
