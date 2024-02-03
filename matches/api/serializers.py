from rest_framework import serializers

from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'tournament', 'date', 'round', 'duration', 'winner', 'loser']
