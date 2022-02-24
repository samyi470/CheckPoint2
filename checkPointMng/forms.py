from django import forms
from django.forms import ModelForm
from .models import Search, DateInput


class SearchForm(ModelForm):
    class Meta:
        model = Search
        widgets = {'start': DateInput(), 'end': DateInput()}
        fields = [
            'terminal',
            'start',
            'end',
        ]
