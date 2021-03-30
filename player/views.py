
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from core.models.invitation import Invitation
from core.models.match_request import MatchRequest
from core.models.registration import Registration
from notifications.models.notification import Notification
from core.models.match import Match
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.contrib import messages

class PlayerInvitationListView(LoginRequiredMixin, ListView):

    model = Invitation
    template_name = "player/invitations.html"


@login_required
def cancel_match_request(request, pk):
    if request.method == "POST":
        match_request = MatchRequest.objects.get_match_request_by_id(pk)
        match_request.cancel()
    messages.success(request, "Invitation annulée!")
    return redirect("index")


@login_required
def decline_match_invitation(request, pk):
    if request.method == "POST":
        invitation_qs = Invitation.objects.get_invitation_by_id(pk)
        invitation = invitation_qs.first()
        invitation.decline()

    messages.success(request, "Invitation déclinée!")
    return redirect("index")


@login_required
def accept_match_invitation(request, pk):
    if request.method == "POST":
        invitation_qs = Invitation.objects.get_invitation_by_id(pk)
        invitation = invitation_qs.first()
        invitation.accept()

        match_id = request.POST.get('match_id')
        match = Match.objects.get(id=match_id)

        try:
            Registration.create_registration(
                match_request=None,
                invitation=invitation,
                player=invitation.for_player,
                match=match,
            )

            Notification.objects.create(
                from_user=invitation.for_player.user,
                to_user=invitation.by_player.user,
                notification_type=2)
        except IntegrityError:
            messages.warning(request, "Vous êtes déjà inscrits dans ce match!")
            return redirect("index")

    messages.success(request, "Vous êtes inscrit dans le match!")
    return redirect("index")
