from django.db import models


class LoaderModel(models.Model):
    matches = models.FileField(help_text='Archivo de partidos')
    players = models.FileField(help_text='Archivo de jugadores')
    stats = models.FileField(help_text='Archivo de datos')
