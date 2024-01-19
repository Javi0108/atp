from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=250)
    hand = models.CharField(max_length=1)
    country = models.CharField(max_length=250)
    birthdate = models.DateField()

    def __str__(self):
        return self.name