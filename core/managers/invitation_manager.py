from django.db import models

from core.querysets.invitation_qs import InvitationQueryset


class InvitationManager(models.Manager):
    def get_queryset(self):
        """This method return the queryset of the Invitation model.

        Returns:
            Queryset: contains all the querysets method for Invitation object.
        """
        return InvitationQueryset(self.model, using=self._db)

    def get_invitation_by_id(self, invitation_id):
        """This method get an invitation by ID.

        Args:
            invitation_id (int): Id of the invitation.

        Returns:
            Queryset: Queryset that contains invitation with id=invitation_id.
        """
        return self.get_queryset().get_invitation_by_id(invitation_id)

    def get_player_invitations(self, player_id):
        """This method get all invitations for a player.

        Args:
            player_id (int): Id of the player.

        Returns:
            Queryset: Queryset that contains invitations of the player.
        """
        return self.get_queryset().get_player_invitations(player_id)

    def get_player_pending_invitations(self, player):
        """This method get an invitation by ID.

        Args:
            invitation_id (int): Id of the invitation.

        Returns:
            Queryset: Queryset that contains invitation with id=invitation_id.
        """
        return self.get_queryset().get_player_pending_invitations(player)

    def count_player_pending_invitations(self, player):
        """This method counts player's invitations with the status 'pending'.

        Args:
            player (object): Player object.

        Returns:
            int: Number of invitation with the status 'pending'.
        """
        return self.get_queryset().count_player_pending_invitations(player)
