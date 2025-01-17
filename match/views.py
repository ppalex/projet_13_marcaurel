from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, View

from api_manager.utils.mapquest_utils import get_address_coordinates
from core.models.address import Address
from core.models.invitation import Invitation
from core.models.location import Location
from core.models.match import Match
from core.models.match_request import MatchRequest
from core.models.player import Player
from core.models.registration import Registration
from player.forms.invitation_form import InvitationFormset
from tasks_manager.tasks import send_alert_email_for_match_task

from .forms.address_creation_form import CustomCreateAddressForm
from .forms.match_creation_form import CreateMatchForm
from .forms.match_update_form import UpdateMatchForm


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

            address = Address.objects.create(
                city=city,
                street=street,
                number=number,
                region=region
            )
            latitude, longitude = get_address_coordinates(
                street, number, city, region)

            match_location = Location.objects.create(
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
                address=address,
                administrator=user.player,
                location=match_location
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


class MatchPlannedListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Match.objects.get_planned_match(administrator=self.request.user.player)


class MatchInProgressListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Match.objects.get_in_progress_match(administrator=self.request.user.player)


class MatchOverListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Match.objects.get_over_match(administrator=self.request.user.player)


class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = "match/match_detail.html"

    def get_context_data(self, **kwargs):

        context = super(MatchDetailView, self).get_context_data(**kwargs)

        match_id = self.kwargs.get("pk")
        match = Match.objects.get_match_by_id(match_id).first()
        context['players'] = self.object.players.all()
        context['player_in_match'] = self.get_object(
        ).match_has_player(self.request.user.player)

        context['requests_count'] = MatchRequest.objects.count_pending_requests(
            match_id)

        context['requests'] = MatchRequest.objects.get_pending_requests(
            match_id)

        context['player_form'] = InvitationFormset()

        context['match_lat'] = float(match.location.lat_lng[0])
        context['match_lon'] = float(match.location.lat_lng[1])

        return context

    def post(self, request, *args, **kwargs):

        player = request.user.player
        match_id = request.POST.get('match_id')
        match = Match.objects.get(id=match_id)

        if request.POST['action'] == "S'inscrire":

            if not match.is_started():

                if not match.is_full():

                    Registration.create_registration(match=match, player=player,
                                                     invitation=None,
                                                     match_request=None)
                    match.add_player()
                    messages.info(
                        request, "Vous vous êtes inscrits dans ce match!")
                else:
                    messages.warning(
                        request, "Les inscriptions sont terminées pour ce match!")
            else:
                messages.warning(
                    request, "Le match a commencé ou est terminé!")

        if request.POST['action'] == "Se désinscrire":
            if not match.is_started():
                registration = Registration.objects.filter(
                    match=match, player=player)

                registration.delete()
                match.remove_player()
                messages.info(
                    request, "Vous vous êtes désinscrits de ce match!")
            else:
                messages.warning(
                    request, "Le match a commencé ou est terminé!")

        if request.POST["action"] == "Demande d'inscription":
            if not match.is_started():
                if not MatchRequest.objects.check_exist_request(status='pending', by_player=player, for_match=match):

                    MatchRequest.objects.create(
                        status="pending",
                        request_date=timezone.now(),
                        by_player=player,
                        for_match=match
                    )
                    messages.info(request, "Votre demande a été envoyée")

                else:
                    messages.warning(request, "Une demande est déjà en cours")

            else:
                messages.warning(
                    request, "Le match a commencé ou est terminé!")

        if request.POST['action'] == "Accepter":
            try:
                if not match.is_started():
                    if not match.is_full():
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
                        match.add_player()
                    else:
                        messages.warning(
                            request, "Les inscriptions sont terminées pour ce match!")

                else:
                    messages.warning(
                        request, "Le match a commencé ou est terminé!")
            except IntegrityError:
                messages.warning(
                    request, "Vous êtes déjà inscrits dans ce match!")
                return redirect("index")

        if request.POST['action'] == "Inviter":
            player_formset = InvitationFormset(request.POST)

            if not match.is_started():
                if player_formset.is_valid():
                    for form in player_formset:
                        player_name = form.cleaned_data.get('player_name')
                        for_player = Player.objects.get_player(
                            player_name).first()
                        if ((player_name) and (for_player not in match.players.all())):
                            Invitation.objects.create(
                                status="pending",
                                invitation_date=timezone.now(),
                                by_player=player,
                                for_player=for_player,
                                for_match=match
                            )
                        else:
                            messages.warning(
                                request, "Invitez des joueurs qui ne sont pas dans le match!")

                            return redirect(f"/match/detail/{match_id}")
                    messages.warning(
                        request, "Les invitations ont été envoyées!")
                    return redirect(f"/match/detail/{match_id}")

                else:
                    self.object = self.get_object()
                    context = self.get_context_data()
                    context['player_form'] = player_formset

                    return render(request, self.template_name, context)
            else:
                messages.warning(
                    request, "Le match a commencé ou est terminé!")

        if request.POST['action'] == "Envoyer l'email":
            if not match.is_started():
                distance = request.POST.get('select_distance')
                match_id = request.POST.get('match_id')
                host_values = {}
                host_values['scheme'] = request.scheme
                host_values['host'] = request.META['HTTP_HOST']
                send_alert_email_for_match_task.delay(
                    match_id, int(distance), host_values)
            else:
                messages.warning(
                    request, "Le match a commencé ou est terminé!")

        return redirect(f"/match/detail/{match_id}")


class MatchSubscriptionPlannedListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_subscription_list.html'
    paginate_by = 4

    def get_queryset(self):
        registrations_qs = Registration.objects.get_opened_registration_for_player(
            player=self.request.user.player)

        return Match.objects.filter(started=False, over=False, id__in=registrations_qs.values('match_id')).exclude(administrator=self.request.user.player)


class MatchSubscriptionInProgressListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_subscription_list.html'
    paginate_by = 4

    def get_queryset(self):
        registrations_qs = Registration.objects.get_opened_registration_for_player(
            player=self.request.user.player)
        return Match.objects.filter(started=True, over=False, id__in=registrations_qs.values('match_id')).exclude(administrator=self.request.user.player)


class MatchSubscriptionOverListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'match/match_subscription_list.html'
    paginate_by = 4

    def get_queryset(self):
        registrations_qs = Registration.objects.get_opened_registration_for_player(
            player=self.request.user.player)
        return Match.objects.filter(started=True, over=True, id__in=registrations_qs.values('match_id')).exclude(administrator=self.request.user.player)


class UpdateMatchView(LoginRequiredMixin, UpdateView):
    model = Match

    template_name = 'match/match_update.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        match = self.get_object()
        if 'match_form' not in kwargs:
            kwargs['match_form'] = UpdateMatchForm(instance=match)

        if 'address_form' not in kwargs:
            kwargs['address_form'] = CustomCreateAddressForm(
                instance=match.address)

        kwargs['match'] = match
        return kwargs

    def form_invalid(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        match = self.get_object()

        match_form = UpdateMatchForm(request.POST, instance=match)

        address_form = CustomCreateAddressForm(
            request.POST, instance=match.address)

        if not match.is_started():

            if match_form.is_valid() and address_form.is_valid():

                city = address_form.cleaned_data['city']
                street = address_form.cleaned_data['street']
                number = address_form.cleaned_data['number']
                region = address_form.cleaned_data['region']

                latitude, longitude = get_address_coordinates(
                    street, number, city, region)

                match.set_location(latitude, longitude)

                match_form.save()
                address_form.save()

                messages.success(request, "Le match a été mis à jour")

                return redirect(f"/match/detail/{match.id}")
            else:

                return self.form_invalid(request, **{'match_form': match_form,
                                                     'address_form': address_form})
        else:
            messages.warning(request, "Le match a commencé ou est terminé!")
            return redirect(f"/match/detail/{match.id}")


@login_required
def cancel_match(request, pk):
    if request.method == "POST":
        match = Match.objects.get_match_by_id(pk).first()
        if not match.is_started():
            match.cancel()
            messages.info(request, "Le match a été supprimé")
            return redirect(reverse("match-planned"))
        else:
            messages.warning(request, "Le match a commencé ou est terminé!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def kick_player(request, pk):
    if request.method == "POST":
        player_id = request.POST.get('player_id')
        player = Player.objects.get_player_by_id(player_id).first()
        match = Match.objects.get_match_by_id(pk).first()
        registration = Registration.objects.filter(
            match=match, player=player)

        registration.delete()
        match.remove_player()
        messages.info(request, "Le joueur a été renvoyé")
        return redirect(f"/match/detail/{pk}")

    return redirect(f"/match/detail/{pk}")
