from django import forms

from core.models.address import Address
from core.models.match import Match
from core.models.player import Player


class MatchFormFilter(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatchFormFilter, self).__init__(*args, **kwargs)
        self.fields['classification'].required = False
        self.fields['start_fixture'].required = False
        self.fields['available_place'].required = False
        self.fields['location'].required = False

    class Meta:
        model = Match
        fields = ('classification', 'start_fixture',
                  'available_place', 'location')

        widgets = {
            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'start_fixture': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'date'}),

            'available_place': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'location': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Entrez le nombre de km"}),

        }


class AddressFormFilter(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressFormFilter, self).__init__(*args, **kwargs)
        self.fields['city'].required = False

    class Meta:
        model = Address
        fields = ('city',)

        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'city-search',
                'type': 'text'}),

        }


class PlayerFormFilter(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(PlayerFormFilter, self).__init__(*args, **kwargs)
        self.fields['location'].required = False

    class Meta:
        model = Player
        fields = ('location',)

        widgets = {
            'location': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Entrez le nombre de km"})
        }
