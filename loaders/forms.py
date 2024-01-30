from django import forms

from .models import LoaderModel


class LoaderForm(forms.ModelForm):
    class Meta:
        model = LoaderModel
        fields = ['players', 'matches', 'stats']
