from django.apps import AppConfig


class BusinessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'business'
    #nazwa w panelu administratora
    verbose_name = "Mój Biznes"
