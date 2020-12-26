
from django.views.generic import ListView

from core.models.invitation import Invitation

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
