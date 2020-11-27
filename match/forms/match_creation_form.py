from django import forms

from core.models.match import Match


class CreateMatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('classification', 'fixture', 'capacity')

        widgets = {
            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'fixture': forms.DateTimeInput(format=('%m/%d/%Y %H:%M'), attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'datetime-local'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }
