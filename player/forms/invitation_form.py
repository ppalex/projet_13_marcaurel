from django import forms
from django.forms import formset_factory

from core.models.player import Player


class InvitationForm(forms.Form):
    player_name = forms.CharField(max_length=255,
                                  label='Nom du joueur',
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'id': 'player-search',
                                      'placeholder': "Chercher un nom"
                                  }),
                                  required=True)

    def clean_player_name(self):

        player_name = self.cleaned_data['player_name']

        if Player.objects.get_player(player_name).count() < 1:
            raise forms.ValidationError("Ce joueur n'existe pas!")

        return player_name


InvitationFormset = formset_factory(InvitationForm)
