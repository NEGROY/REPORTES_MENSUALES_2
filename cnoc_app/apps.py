from django.apps import AppConfig


class CnocAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cnoc_app'

    def ready(self):
        # Import explícito de submódulos de modelos
        import cnoc_app.escalacion.models
        import cnoc_app.asientos.models
        import cnoc_app.retroalimentacion.models
