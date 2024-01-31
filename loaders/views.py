import csv
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from matches.models import Match, Stats
from players.models import Player

from .forms import LoaderForm


@csrf_exempt
def get_datos(request):
    if request.method == 'POST':
        form = LoaderForm(request.POST, request.FILES)
        if form.is_valid():
            for files in request.FILES:
                print(request.FILES)
                with open('atp-data/' + files + '.csv', 'r') as file:
                    csvreader = csv.reader(file)
                    header = next(csvreader)
                    print(header)
                    for row in csvreader:
                        if files == 'players':
                            # for row in csvreader:
                            player = Player()
                            player.name = row[1]
                            player.hand = row[2]
                            player.country = row[3]
                            player.birthdate = datetime.strptime(row[4], '%Y-%m-%d').date()
                            player.save()

                        elif files == 'matches':
                            # for row in csvreader:
                            match = Match()
                            match.tournament = row[1]
                            match.date = datetime.strptime(row[2], '%Y-%m-%d').date()
                            match.round = row[3]
                            match.duration = int(row[4])

                            # Obtén los jugadores ganador y perdedor
                            winner = Player.objects.get(name=row[5])
                            loser = Player.objects.get(name=row[6])

                            # Crea los objetos Stats y guarda la relación con partido y jugadores.
                            winner_stats = Stats(match_id=match, player_id=winner, winner=True)
                            winner_stats.save()

                            loser_stats = Stats(match_id=match, player_id=loser, winner=False)
                            loser_stats.save()
                            match.save()

                        elif files == 'stats':
                            # for row in csvreader:
                            match = Match.objects.get(id=int(row[0]))
                            player = Player.objects.get(name=row[1])
                            winner = bool(row[2])

                            # Crea el objeto Stats y guarda la relación con el partido y el jugador
                            stats = Stats(match_id=match, player_id=player, winner=winner)
                            stats.save()
            return JsonResponse({'status': 'ok'})
    else:
        form = LoaderForm()
    return render(request, 'loader/index.html', {'form': form})
