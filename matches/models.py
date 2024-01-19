from django.db import models

from players.models import Player


class Match(models.Model):
    tournament = models.CharField(max_length=250)
    date = models.DateField()
    round = models.CharField(max_length=250)
    duration = models.IntegerField()
    winner = models.ForeignKey(Player, related_name='win_matches', on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, related_name='lost_matches', on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament
