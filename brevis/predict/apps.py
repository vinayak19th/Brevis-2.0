from json import decoder
from django.apps import AppConfig

class PredictConfig(AppConfig):
    """Class to get predictions from text off the TF Serving server
    """
    name = 'predict'

class NewsConfig(AppConfig):
    name = 'newspaper'