from django import forms
from django.utils import timezone
from core.models.match import Match


class CreateMatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('classification', 'start_fixture', 'end_fixture', 'capacity')

        widgets = {
            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'start_fixture': forms.DateTimeInput(format=('%Y-%m-%d %H:%M'),
                                                 attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'datetime-local'}),

            'end_fixture': forms.DateTimeInput(format=('%Y-%m-%d %H:%M'),
                                               attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'datetime-local'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }

    def clean_start_fixture(self):
        start_fixture = self.cleaned_data['start_fixture']

        if start_fixture < timezone.now():
            raise forms.ValidationError(
                "La date ne peut pas être dans le passé!")
        return start_fixture

    def clean_end_fixture(self):
        end_fixture = self.cleaned_data['end_fixture']

        if end_fixture < timezone.now():
            raise forms.ValidationError(
                "La date ne peut pas être dans le passé!")

        if end_fixture < self.cleaned_data['start_fixture']:
            raise forms.ValidationError(
                "Chosissez des valeurs après le coup d'envoi du match!")

        return end_fixture
