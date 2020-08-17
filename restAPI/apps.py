from django.apps import AppConfig


class RestapiConfig(AppConfig):
    name = 'restAPI'

    def ready(self):#import django-signals
        import restAPI.signals
