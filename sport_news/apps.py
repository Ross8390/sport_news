from django.apps import AppConfig


class SportNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sport_news'

    def ready(self):
        import sport_news.signals
