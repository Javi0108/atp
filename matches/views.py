from rest_framework import generics

from matches.api.serializers import MatchSerializer
from matches.models import Match
from players.api.serializers import PlayerSerializer
from players.models import Player


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchWinnerLoserDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
