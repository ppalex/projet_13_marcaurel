from django.views.generic.edit import CreateView

from core.models.player import Player

from .forms import PlayerCreateForm


class CreatePlayerView(CreateView):
    form_class = PlayerCreateForm
    model = Player

    template_name = 'player/player_creation.html'
