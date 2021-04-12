from django.db import models


class InvitationQueryset(models.QuerySet):

    def get_invitation_by_id(self, invitation_id):
        """This method get an invitation by ID.

        Args:
            invitation_id (int): Id of the invitation.

        Returns:
            Queryset: Queryset that contains invitation with id=invitation_id.
        """
        return self.filter(id=invitation_id)

    def get_player_invitations(self, player_id):
        """This method get all invitations for a player.

        Args:
            player_id (int): Id of the player.

        Returns:
            Queryset: Queryset that contains invitations of the player.
        """
        return self.filter(for_player=player_id)

    def get_player_pending_invitations(self, player):
        return self.filter(status='pending', for_player=player)

    def count_player_pending_invitations(self, player):
        """This method counts player's invitations with the status 'pending'.

        Args:
            player (object): Player object.

        Returns:
            int: Number of invitation with the status 'pending'.
        """
        return self.filter(status='pending', for_player=player).count()
