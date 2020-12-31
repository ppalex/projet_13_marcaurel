from django.db import models
from search_manager.utils import km_to_degrees


class PlayerQueryset(models.QuerySet):
    def get_player_name_start_with(self, term):
        return self.filter(user__username__startswith=term)

    def get_player(self, player_name):
        return self.filter(user__username=player_name)

    def get_player_dwithin(self, geom_object, distance):
        return self.filter(location__coordinates__dwithin=(geom_object,
                                                           km_to_degrees(distance)))
