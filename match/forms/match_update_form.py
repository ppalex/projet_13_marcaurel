from django import forms

from .match_creation_form import CreateMatchForm


class UpdateMatchForm(CreateMatchForm):
    class Meta(CreateMatchForm.Meta):
        fields = ('classification', 'start_fixture', 'end_fixture', 'capacity')

        widgets = {

            'classification': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text'}),

            'start_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text'}),

            'end_fixture': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text'}),

            'capacity': forms.Select(choices=[(x, x) for x in range(8, 21)],
                                     attrs={
                'class': 'form-control',
                'type': 'text'}),

        }

    def clean_capacity(self):

        capacity = self.cleaned_data['capacity']
        match = self.instance

        if capacity < match.num_player:
            raise forms.ValidationError(
                "Impossible de réduire le nombre de joueur. Il y a déjà trop de joueur inscrit!")
        return capacity

    def save(self, commit=True):
        instance = super(UpdateMatchForm, self).save(commit=False)

        instance.update_full_status()

        if instance.num_player < instance.capacity:
            instance.available_place = instance.capacity - instance.num_player
        elif instance.num_player > instance.capacity:
            instance.available_place = instance.num_player - instance.capacity
        else:
            pass

        if commit:
            instance.save()
