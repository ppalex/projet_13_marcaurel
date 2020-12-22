from django.db import models
from core.querysets.invitation_qs import InvitationQueryset


class InvitationManager(models.Manager):
    def get_queryset(self):
        return InvitationQueryset(self.model, using=self._db)

    def get_player_invitations(self, player_id):
        self.get_queryset().get_player_invitations(player_id)
