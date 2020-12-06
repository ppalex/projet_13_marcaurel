from django import forms
from core.models.match import Match
from core.models.address import Address


class MatchFormFilter(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatchFormFilter, self).__init__(*args, **kwargs)
        self.fields['classification'].required = False
        self.fields['fixture'].required = False
        self.fields['available_place'].required = False

    class Meta:
        model = Match
        fields = ('classification', 'fixture', 'available_place',)

        widgets = {
            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'fixture': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'date'}),

            'available_place': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'text'}),

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
                'type': 'text'}),

        }
