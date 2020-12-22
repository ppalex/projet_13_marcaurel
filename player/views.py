
from django.views.generic import ListView

from core.models.invitation import Invitation

from django.contrib.auth.mixins import LoginRequiredMixin


class PlayerInvitationListView(LoginRequiredMixin, ListView):

    model = Invitation
    template_name = "player/invitations.html"
