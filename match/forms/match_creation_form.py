from django import forms
from django.utils import timezone
from core.models.match import Match


class CreateMatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('classification', 'fixture', 'capacity')

        widgets = {
            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'fixture': forms.DateTimeInput(format=('%Y-%m-%d %H:%M'), attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'datetime-local'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }

    def clean_fixture(self):
        fixture = self.cleaned_data['fixture']

        if fixture < timezone.now():
            raise forms.ValidationError(
                "La date ne peut pas être dans le passé!")
        return fixture
