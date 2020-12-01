from django.db import models

from core.models.invitation import Invitation
from core.models.player import Player
from core.models.match import Match
from core.models.match_request import MatchRequest

from django.utils import timezone


class Registration(models.Model):
    join_date = models.DateTimeField(null=True, blank=True)

    invitation = models.OneToOneField(
        Invitation, on_delete=models.CASCADE, null=True, blank=True)

    match_request = models.OneToOneField(
        MatchRequest, on_delete=models.CASCADE, null=True, blank=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=None)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default=None)

    @classmethod
    def create_registration(cls, match, player, invitation, match_request):

        now = timezone.now()

        registration = cls(join_date=now,
                           invitation=invitation,
                           match_request=match_request,
                           player=player,
                           match=match)

        registration.save()
