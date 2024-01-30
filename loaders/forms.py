from django import forms

from .models import LoaderModel


class LoaderForm(forms.ModelForm):
    class Meta:
        model = LoaderModel
        input_format = '%Y-%m-%d'
        fields = ['players', 'matches', 'stats']
