from django.db import models


class InvitationQueryset(models.QuerySet):

    def get_player_invitations(self, player_id):
        return self.filter(for_player=player_id)

    def get_player_pending_invitations(self, player):
        return self.filter(status='pending', for_player=player)

    def count_player_pending_invitations(self, player):
        return self.filter(status='pending', for_player=player).count()
    