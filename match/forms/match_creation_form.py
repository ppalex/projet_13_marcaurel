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

            'start_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'}),

            'end_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }

    def clean_start_fixture(self):
        start_fixture = self.cleaned_data.get('start_fixture')
        if start_fixture:
            if start_fixture < timezone.now():
                raise forms.ValidationError(
                    "Le coup d'envoi ne peut pas être dans le passé!")
            return start_fixture

    def clean_end_fixture(self):
        end_fixture = self.cleaned_data.get('end_fixture')
        if end_fixture:
            if end_fixture < timezone.now():
                raise forms.ValidationError(
                    "La fin du match ne peut pas être dans le passé!")
            return end_fixture

    def clean(self):
        cleaned_data = self.cleaned_data
        end_fixture = cleaned_data.get('end_fixture')
        start_fixture = cleaned_data.get('start_fixture')
        if end_fixture and start_fixture:
            if end_fixture < start_fixture:
                self.add_error(
                    'end_fixture', "Choisissez une heure après le coup d'envoi!")
            return cleaned_data
