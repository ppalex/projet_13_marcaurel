from django.shortcuts import render

from django.views.generic import View

from core.models.match import Match
from core.models.player import Player


from .forms import MatchFormFilter, AddressFormFilter

import django_tables2 as tables

from .tables import MatchTable

from django.contrib.auth.mixins import LoginRequiredMixin


class SearchMapMatchView(LoginRequiredMixin, View):

    template_name = "search_manager/search_map_match.html"

    def get(self, request, *args, **kwargs):

        context = {}
        context['match_filter'] = MatchFormFilter()
        context['address_filter'] = AddressFormFilter()
        context['object_list'] = Match.objects.all()

        return render(request, self.template_name, context)


class SearchTableMatchView(LoginRequiredMixin, tables.SingleTableView):
    table_class = MatchTable
    queryset = Match.objects.all()

    template_name = "search_manager/search_table_match.html"


class SearchMapPlayerView(LoginRequiredMixin, View):
    template_name = "search_manager/search_map_player.html"

    def get(self, request, *args, **kwargs):

        context = {}
        context['object_list'] = Player.objects.get_all_player_with_location_except_current(
            request.user)

        return render(request, self.template_name, context)
