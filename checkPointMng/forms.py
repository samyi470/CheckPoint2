from django import forms
from django.forms import ModelForm
from .models import Search, DateInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Column, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class SearchForm(ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    helper.layout = Layout(
        Div(
            Div(
                'terminal',
                css_class='col-xs-12 col-md-6'
            ),
            Div(
                'start',
                css_class='col-sm-6 col-md-3'
            ),
            Div(
                'end',
                css_class='col-sm-6 col-md-3'
            ),
            css_class='row p-3 d-flex justify-content-center'
        ),
        Div(
            Div(
                Submit('submit', 'Submit'),
                css_class='col-auto'
            ),
            css_class='row pb-3 d-flex justify-content-center'
        )
    )

    class Meta:
        model = Search
        widgets = {'start': DateInput(), 'end': DateInput()}
        fields = [
            'terminal',
            'start',
            'end',
        ]
