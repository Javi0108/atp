import csv

from django.shortcuts import render

from .forms import LoaderForm


def get_datos(request):
    if request.method == 'POST':
        form = LoaderForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            # Aquí puedes realizar el procesamiento del archivo CSV
            # lista_archivos = [request.FILES]
            rows = []
            for files in request.FILES:
                with open(files, 'r') as file:
                    csvreader = csv.reader(file)
                    # header = next(csvreader)
                    for row in csvreader:
                        rows.append(row)
                # print(header)
                print(rows[1])
            # utilizando la instancia del modelo
    else:
        form = LoaderForm()
    return render(request, 'loader/index.html', {'form': form})
