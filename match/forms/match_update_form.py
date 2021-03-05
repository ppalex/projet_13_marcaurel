from .match_creation_form import CreateMatchForm
from django import forms


class UpdateMatchForm(CreateMatchForm):
    class Meta(CreateMatchForm.Meta):
        fields = ('classification', 'start_fixture', 'end_fixture', 'capacity')

        widgets = {

            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'start_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text'}),

            'end_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }
