from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from core.forms import AddressCreateForm
from core.models.match import Match
from core.models.address import Address
from .forms.match_creation_form import CreateMatchForm


class CreateMatchView(View, LoginRequiredMixin):
    template_name = 'match/match_creation.html'

    def get_context_data(self,  **kwargs):
        if 'match_form' not in kwargs:
            kwargs['match_form'] = CreateMatchForm()

        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm()

        return kwargs

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        match_form = CreateMatchForm(request.POST)
        address_form = AddressCreateForm(request.POST)

        print(match_form.errors)
        print(match_form.errors)
        if match_form.is_valid() and address_form.is_valid():

            user = request.user

            city = address_form.cleaned_data['city']
            street = address_form.cleaned_data['street']
            number = address_form.cleaned_data['number']
            region = address_form.cleaned_data['region']

            address = Address.objects.get_or_create(
                city=city,
                street=street,
                number=number,
                region=region
            )

            match = Match.objects.create(

                num_player=1,
                fixture=match_form.cleaned_data['fixture'],
                capacity=match_form.cleaned_data['capacity'],
                full=False,
                started=False,
                cancelled=False,
                over=False,
                address=address[0],
                administrator=user.player
            )
            match.save()

            return render(request, self.template_name, self.get_context_data())

        else:

            return render(request, self.template_name, self.get_context_data())
