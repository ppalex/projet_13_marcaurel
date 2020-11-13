from django.db import models

from core.models.player import Player
from core.models.match import Match


class Invitation(models.Model):

    STATUS_CHOICES = (('pending', 'En attente'),
                      ('accepted', 'Accepté'), ('refused', 'Refusé'))

    status = models.TextField(max_length=255, choices=STATUS_CHOICES)
    invitation_date = models.DateTimeField()
    response_date = models.DateTimeField(null=True, blank=True)

    by_player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='by_player')

    for_player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='for_player')

    for_match = models.ForeignKey(Match, on_delete=models.CASCADE)
