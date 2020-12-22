from django.db import models


class PlayerQueryset(models.QuerySet):
    def get_player_name_start_with(self, term):
        return self.filter(user__username__startswith=term)
