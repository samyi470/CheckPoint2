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
        Row(
            Column('terminal', css_class='form-group col-6'),
            Column('start', css_class='form-group col-3'),
            Column('end', css_class='form-group col-3'),
            css_class='form-row'
        ),
        Div(
            Submit('submit', 'Submit'),
            css_class='d-flex justify-content-center'
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
