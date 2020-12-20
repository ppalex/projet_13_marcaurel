from django.db import models

from core.models.invitation import Invitation
from core.models.player import Player
from core.models.match import Match
from core.models.match_request import MatchRequest

from core.managers.registration_manager import RegistrationManager

from django.utils import timezone


class Registration(models.Model):

    STATUS_CHOICES = (('opened', 'Ouvert'),
                      ('closed', 'Clôturé'))

    status = models.TextField(max_length=15, choices=STATUS_CHOICES)
    join_date = models.DateTimeField(null=True, blank=True)

    invitation = models.OneToOneField(
        Invitation, on_delete=models.CASCADE, null=True, blank=True)

    match_request = models.OneToOneField(
        MatchRequest, on_delete=models.CASCADE, null=True, blank=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=None)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default=None)

    objects = RegistrationManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['player', 'match'], name='unique_player_for_match')
        ]

    @classmethod
    def create_registration(cls, match, player, invitation, match_request):

        now = timezone.now()

        registration = cls(
            status="opened",
            join_date=now,
            invitation=invitation,
            match_request=match_request,
            player=player,
            match=match)

        registration.save()
