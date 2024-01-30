import csv

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
            # Aquí puedes realizar el procesamiento del archivo CSV
            # lista_archivos = [request.FILES]
            # players_rows = []
            # matches_rows = []
            # stats_rows = []

            for files in request.FILES:
                print(files)
                with open('atp-data/' + files + '.csv', 'r') as file:
                    csvreader = csv.reader(file)
                    # header = next(csvreader)
                    for row in csvreader:
                        if files == 'players':
                            Player.objects.create(
                                # player_id=row[0],
                                name=row[1],
                                hand=row[2],
                                country=row[3],
                                birthdate=[4],
                            )
                        elif files == 'matches':
                            Match.objects.create(
                                # match_id=row[0],
                                tournament=row[1],
                                date=row[2],
                                round=row[3],
                                duration=[4],
                            )
                        elif files == 'stats':
                            Stats.objects.create(
                                match_id=row[0],
                                player_id=[1],
                                winner=[2],
                            )

                return JsonResponse({'status': 'ok'})
        # utilizando la instancia del modelo
    else:
        form = LoaderForm()
    return render(request, 'loader/index.html', {'form': form})
