from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models.location import Location
from core.models.match import Match
from core.models.address import Address
from .forms.match_creation_form import CreateMatchForm
from .forms.address_creation_form import CustomCreateAddressForm

from django.contrib.gis.geos import Point

from apiManager.utils.mapquest_utils import get_address_coordinates
from django.contrib import messages

from django.views.generic import ListView, DetailView

from core.models.registration import Registration


class CreateMatchView(View, LoginRequiredMixin):
    template_name = 'match/match_creation.html'

    def get_context_data(self,  **kwargs):
        if 'match_form' not in kwargs:
            kwargs['match_form'] = CreateMatchForm()

        if 'address_form' not in kwargs:
            kwargs['address_form'] = CustomCreateAddressForm()

        return kwargs

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        match_form = CreateMatchForm(request.POST)
        address_form = CustomCreateAddressForm(request.POST)

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

            latitude, longitude = get_address_coordinates(
                street, number, city, region)

            match_location = Location.objects.get_or_create(
                coordinates=Point(longitude, latitude, srid=4326)
            )

            match = Match.objects.create(

                num_player=1,
                classification=match_form.cleaned_data['classification'],
                fixture=match_form.cleaned_data['fixture'],
                capacity=match_form.cleaned_data['capacity'],
                available_place=match_form.cleaned_data['capacity']-1,
                full=False,
                started=False,
                cancelled=False,
                over=False,
                address=address[0],
                administrator=user.player,
                location=match_location[0]
            )
            match.save()

            Registration.create_registration(match=match, player=user.player,
                                             invitation=None, match_request=None)

            messages.success(request, "Votre match a été créé!")

            return render(request, self.template_name, self.get_context_data())

        else:
            context = {
                'match_form': match_form,
                'address_form': address_form
            }

            return render(request, self.template_name, context)


class MatchListView(ListView):
    model = Match
    template_name = 'match/match_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Match.objects.filter(administrator=self.request.user.player)


class MatchDetailView(DetailView):
    model = Match
    template_name = "match/match_detail.html"

    def get_object(self):
        id = self.kwargs.get("id")

        return get_object_or_404(Match, id=id)

    def get_context_data(self, **kwargs):

        context = super(MatchDetailView, self).get_context_data(**kwargs)

        context['players'] = self.object.players.all()
        return context
