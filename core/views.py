from django.shortcuts import render

from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.models.invitation import Invitation
from core.models.match_request import MatchRequest


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'core/base.html'

    def get_context_data(self, **kwargs):
        player = self.request.user.player
        context = super().get_context_data(**kwargs)

        context['invitations_count'] = Invitation.objects.count_player_pending_invitations(
            player)
        context['invitations'] = Invitation.objects.get_player_pending_invitations(
            player)

        context['requests_count'] = MatchRequest.objects.count_player_pending_requests(
            player)
        context['requests'] = MatchRequest.objects.get_player_pending_requests(
            player)

        return context


def custom_page_not_found_view(request, exception):
    return render(request, "core/404.html", {})
