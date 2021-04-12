from django.db import models

from core.querysets.invitation_qs import InvitationQueryset


class InvitationManager(models.Manager):
    def get_queryset(self):
        return InvitationQueryset(self.model, using=self._db)

    def get_invitation_by_id(self, invitation_id):
        return self.get_queryset().get_invitation_by_id(invitation_id)

    def get_player_invitations(self, player_id):
        return self.get_queryset().get_player_invitations(player_id)

    def get_player_pending_invitations(self, player):
        return self.get_queryset().get_player_pending_invitations(player)

    def count_player_pending_invitations(self, player):
        return self.get_queryset().count_player_pending_invitations(player)
