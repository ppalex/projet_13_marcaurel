import datetime

from .models.address import Address

from django import forms


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('city', 'street', 'number', 'region')

        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Ville"}),

            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Rue"}),

            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Numéro"}),

            'region': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Région"}),

        }

    def clean_fixture(self):
        fixture = self.cleaned_data['fixture']
        if fixture < datetime.date.today():
            raise forms.ValidationError(
                "La date ne peut pas être dans le passé!")
        return fixture
