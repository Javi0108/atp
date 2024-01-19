from django import forms


class LoaderForm(forms.Form):
    matches = forms.FileField(label='Archivo de partidos')
    players = forms.FileField(label='Archivo de jugadores')
    stats = forms.FileField(label='Archivo de datos')
