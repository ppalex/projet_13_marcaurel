from django.views.generic.edit import CreateView
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from core.models.player import Player

from .forms import PlayerCreateForm
from core.forms import AddressCreateForm


# class CreatePlayerView(CreateView):
#     form_class = PlayerCreateForm
#     model = Player

#     template_name = 'player/player_creation.html'


class CreatePlayerView(View):
    template_name = 'player/player_creation.html'

    def get_context_data(self,  **kwargs):
        if 'player_form' not in kwargs:
            kwargs['player_form'] = PlayerCreateForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        context = {}

        player_form = PlayerCreateForm(request.POST)
        address_form = AddressCreateForm(request.POST)
        print(player_form.errors)
        print(address_form.is_valid())
        if player_form.is_valid() and address_form.is_valid():

            pass

        else:
            print('nok')
            context['player_form'] = player_form
            context['address_form'] = address_form

            return render(request, self.template_name, context)
