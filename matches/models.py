from django.db import models

from players.models import Player


class Match(models.Model):
    match_id = models.CharField(max_length=10)
    tournament = models.CharField(max_length=250)
    date = models.DateTimeField(blank=True, null=True)
    round = models.CharField(max_length=250)
    duration = models.IntegerField()
    winner = models.ForeignKey(Player, related_name='win_matches', on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, related_name='lost_matches', on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament


# class Stats(models.Model):
#     match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
#     player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
#     winner = models.BooleanField()
