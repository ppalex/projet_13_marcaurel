

from django import forms

from .models.address import Address


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
