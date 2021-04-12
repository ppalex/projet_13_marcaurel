from django.db import models

from core.managers.invitation_manager import InvitationManager
from core.models.match import Match
from core.models.player import Player


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

    objects = InvitationManager()

    def accept(self):
        """This method change the status of invitation to 'accepted'.
        """
        self.status = 'accepted'
        self.save()

    def decline(self):
        """This method change the status of invitation to 'refused'.
        """
        self.status = 'refused'
        self.save()
