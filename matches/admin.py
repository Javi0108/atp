from django.contrib import admin

from .models import Match, Stats


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'date', 'round', 'duration', 'winner', 'loser']


@admin.register(Stats)
class StatAdmin(admin.ModelAdmin):
    list_display = ['match_id', 'player_id', 'winner']
