from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models.player import Player
from core.models.location import Location
from core.models.match import Match
from core.models.address import Address
from core.models.match_request import MatchRequest
from core.models.invitation import Invitation

from .forms.match_creation_form import CreateMatchForm
from .forms.address_creation_form import CustomCreateAddressForm

from django.contrib.gis.geos import Point

from api_manager.utils.mapquest_utils import get_address_coordinates
from django.contrib import messages

from django.views.generic import ListView, DetailView

from core.models.registration import Registration
from core.models.match import Match

from django.shortcuts import redirect

from django.utils import timezone

from player.forms.invitation_form import InvitationForm, InvitationFormset

import pdb


class CreateMatchView(LoginRequiredMixin, View):
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
                start_fixture=match_form.cleaned_data['start_fixture'],
                end_fixture=match_form.cleaned_data['end_fixture'],
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


class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Match.objects.filter(administrator=self.request.user.player)


class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = "match/match_detail.html"

    def get_context_data(self, **kwargs):

        context = super(MatchDetailView, self).get_context_data(**kwargs)

        match_id = self.kwargs.get("pk")
        context['players'] = self.object.players.all()
        context['player_in_match'] = self.get_object(
        ).match_has_player(self.request.user.player)

        context['requests_count'] = MatchRequest.objects.count_pending_requests(
            match_id)

        context['requests'] = MatchRequest.objects.get_pending_requests(
            match_id)

        context['player_form'] = InvitationFormset()

        return context

    def post(self, request, *args, **kwargs):

        player = request.user.player
        match_id = request.POST.get('match_id')
        match = Match.objects.get(id=match_id)

        if request.POST['action'] == "S'inscrire":

            Registration.create_registration(match=match, player=player,
                                             invitation=None,
                                             match_request=None)

            messages.info(request, "Vous vous êtes inscrit dans ce match!")

        if request.POST['action'] == "Se désinscrire":

            registration = Registration.objects.filter(
                match=match, player=player)

            registration.delete()

            messages.info(request, "Vous vous êtes désinscrit de ce match!")

        if request.POST["action"] == "Demande d'inscription":

            MatchRequest.objects.create(
                status="pending",
                request_date=timezone.now(),
                by_player=player,
                for_match=match
            )
            messages.info(request, "Votre demande a été envoyée")

        if request.POST['action'] == "Accepter":
            request_id = request.POST.get('request_id')
            match_request = MatchRequest.objects.get_request(
                request_id)
            match_request.update(status="accepted")

            Registration.create_registration(
                match_request=match_request.first(),
                invitation=None,
                player=match_request.first().by_player,
                match=match,
            )

        if request.POST['action'] == "Inviter":
            player_formset = InvitationFormset(request.POST)

            if player_formset.is_valid():
                for form in player_formset:

                    if form.cleaned_data.get('player_name'):
                        Invitation.objects.create(
                            status="pending",
                            invitation_date=timezone.now(),
                            by_player=player,
                            for_player=Player.objects.get_player(
                                form.cleaned_data.get('player_name')).first(),
                            for_match=match
                        )

                return redirect(f"/match/detail/{match_id}")

            else:
                self.object = self.get_object()
                context = self.get_context_data()
                context['player_form'] = player_formset

                return render(request, self.template_name, context)

        return redirect(f"/match/detail/{match_id}")


class MatchSubscriptionListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_subscription_list.html'
    paginate_by = 4

    def get_queryset(self):

        player = self.request.user.player

        return player.match_set.all()
