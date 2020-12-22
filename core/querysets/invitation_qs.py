from django.db import models


class InvitationQueryset(models.QuerySet):

    def get_player_invitations(self, player_id):
        self.filter(for_player=player_id)
