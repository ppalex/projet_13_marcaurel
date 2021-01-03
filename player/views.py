
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from core.models.invitation import Invitation
from core.models.match_request import MatchRequest
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin


class PlayerInvitationListView(LoginRequiredMixin, ListView):

    model = Invitation
    template_name = "player/invitations.html"


class PlayerSendInvitation(LoginRequiredMixin):

    model = Invitation
    template_name = "player/invitations.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerInvitationListView,
                        self).get_context_data(**kwargs)

        return context


@login_required
def cancel_match_request(request, pk):
    if request.method == "POST":
        match_request = MatchRequest.objects.get_match_request_by_id(pk)
        match_request.cancel()

    return redirect("index")


@login_required
def decline_match_invitation(request, pk):
    if request.method == "POST":
        invitation_qs = Invitation.objects.get_invitation_by_id(pk)
        invitation = invitation_qs.first()
        invitation.decline()

    return redirect("index")
