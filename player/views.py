from django.views.generic.edit import CreateView
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from core.models.player import Player
from core.models.address import Address


from users.models.user import User

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

            user = User.objects.get(username="admin")

            city = address_form.cleaned_data['city']
            street = address_form.cleaned_data['street']
            number = address_form.cleaned_data['number']
            region = address_form.cleaned_data['region']

            address = Address.objects.create(
                city=city,
                street=street,
                number=number,
                region=region
            )

            address.save()

            firstname = player_form.cleaned_data['firstname']
            name = player_form.cleaned_data['name']
            birthdate = player_form.cleaned_data['birthdate']
            sex = player_form.cleaned_data['sex']
            level = player_form.cleaned_data['level']
            positions = player_form.cleaned_data['positions']

            player = Player.objects.create(firstname=firstname,
                                           name=name,
                                           birthdate=birthdate,
                                           sex=sex,
                                           level=level,
                                           address=address,
                                           user=user)

            player.positions.add(*positions)
            player.save()

            return render(request, self.template_name, context)

        else:
            context['player_form'] = player_form
            context['address_form'] = address_form

            return render(request, self.template_name, context)
