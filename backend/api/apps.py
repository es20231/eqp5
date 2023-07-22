from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self, *args, **kwargs) -> None:
        from api import signals
        return super().ready(*args, **kwargs)