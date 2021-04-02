from .match_creation_form import CreateMatchForm
from django import forms


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

    def save(self, commit=True, **kwargs):

        available_place = kwargs.get('available_place')
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
