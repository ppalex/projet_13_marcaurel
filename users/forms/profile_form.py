from django import forms

from core.models.address import Address

from core.models.player import Player

from django import forms


class PlayerCreateForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('firstname', 'name', 'birthdate',
                  'sex', 'level', 'positions')

        LEVEL_CHOICES = (('novice', 'Débutant'),
                         ('intermediate', 'Intermédiaire'),
                         ('advanced', 'Avancé'))

        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Prénom"}),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Nom"}),

            'birthdate': forms.SelectDateWidget(attrs={
                'class': 'form-control'}),


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
