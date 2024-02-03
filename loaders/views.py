import csv

# from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from matches.models import Match
from players.models import Player

from .forms import LoaderForm


@csrf_protect
def get_datos(request):
    if request.method == 'POST':
        form = LoaderForm(request.POST, request.FILES)
        if form.is_valid():
            # Aquí puedes realizar el procesamiento del archivo CSV
            # lista_archivos = [request.FILES]
            # players_rows = []
            # matches_rows = []
            stats_rows = []

            for files in request.FILES:
                print(files)
                with open('atp-data/' + files + '.csv', 'r') as file:
                    csvreader = csv.reader(file)
                    # header = next(csvreader)
                    for row in csvreader:
                        if files == 'players':
                            Player.objects.get_or_create(
                                player_id=row[0],
                                name=row[1],
                                hand=row[2],
                                country=row[3],
                                birthdate=[4],
                            )
                        elif files == 'matches':
                            Match.objects.get_or_create(
                                match_id=row[0],
                                tournament=row[1],
                                date=row[2],
                                round=row[3],
                                duration=[4],
                                winner=[5],
                                loser=[6],
                            )
                        elif files == 'stats':
                            stats_rows.append(row)

                    # print(header)
                    # print(players_rows)
                    # print(matches_rows)
                    # print(stats_rows)

            # return JsonResponse({'status': 'ok'})
        # utilizando la instancia del modelo
    else:
        form = LoaderForm()
    return render(request, 'loader/index.html', {'form': form})
