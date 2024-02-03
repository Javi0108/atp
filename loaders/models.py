from django.db import models


class LoaderModel(models.Model):
    players = models.FileField(help_text='Archivo de jugadores')
    matches = models.FileField(help_text='Archivo de partidos')
    stats = models.FileField(help_text='Archivo de datos')
