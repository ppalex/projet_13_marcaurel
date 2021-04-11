from django.db import models

from core.managers.match_request_manager import MatchRequestManager
from core.models.match import Match
from core.models.player import Player


class MatchRequest(models.Model):

    STATUS_CHOICES = (('pending', 'En attente'),
                      ('accepted', 'Accepté'), ('refused', 'Refusé'))

    status = models.TextField(max_length=255, choices=STATUS_CHOICES)
    request_date = models.DateTimeField()
    response_date = models.DateTimeField(null=True, blank=True)

    by_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    for_match = models.ForeignKey(Match, on_delete=models.CASCADE)

    objects = MatchRequestManager()

    def cancel(self):
        self.delete()
