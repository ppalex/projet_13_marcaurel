from django import forms

from core.models.address import Address
from users.models.profile import Profile


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('firstname', 'name', 'birthdate',
                  'sex', 'level', 'positions')

        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Prénom"}),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Nom"}),

            'birthdate': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Choisissez une date',
                'type': 'date'}),

            'level': forms.Select(attrs={
                'class': 'form-control'}),

            'sex': forms.Select(attrs={
                'class': 'form-control'}),

            'positions': forms.CheckboxSelectMultiple()

        }


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
