from django.db import models


class LoaderModel(models.Model):
    matches = models.FileField(help_text='Archivo de partidos')
    stats = models.FileField(help_text='Archivo de datos')
    players = models.FileField(help_text='Archivo de jugadores')
