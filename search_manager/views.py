from django.shortcuts import render

from django.views.generic import ListView

from core.models.match import Match


class MapView(ListView):
    model = Match
    template_name = "search_manager/search_map.html"
