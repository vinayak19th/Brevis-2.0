from django.apps import AppConfig
from .paper import get_articles

class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'