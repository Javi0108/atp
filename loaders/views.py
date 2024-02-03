import csv
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from matches.models import Match
from players.models import Player

from .forms import LoaderForm


@csrf_exempt
def get_datos(request):
    if request.method == 'POST':
        form = LoaderForm(request.POST, request.FILES)
        if form.is_valid():
            for files in request.FILES:
                with open(files + '.csv', 'r') as file:
                    next(file)  # Salta la primera linea del archivo
                    csvreader = csv.reader(file)
                    print(file.name)
                    for row in csvreader:
                        if file.name == 'players.csv':
                            player = Player()
                            player.name = row[1]
                            player.hand = row[2]
                            player.country = row[3]
                            player.birthdate = datetime.strptime(row[4], '%Y-%m-%d')
                            player.save()

                        elif file.name == 'matches.csv':
                            match = Match()
                            match.tournament = row[1]
                            match.date = datetime.strptime(row[2], '%Y-%m-%d')
                            match.round = row[3]
                            match.duration = row[4]
                            match.save()

                            # Falta hacer que los campos winner y loser se puedan insertar en la tabla matches

                        elif file.name == 'stats.csv':
                            match_id = row[0]
                            player_id = row[1]
                            winner = bool(row[2])
            return JsonResponse({'status': 'ok'})
    else:
        form = LoaderForm()
    return render(request, 'loader/index.html', {'form': form})
