from django.db import models
from search_manager.utils import km_to_degrees


class PlayerQueryset(models.QuerySet):
    def get_player_name_start_with(self, term):
        return self.filter(user__username__startswith=term)

    def get_player(self, player_name):
        return self.filter(user__username=player_name)

    def get_player_by_id(self, player_id):
        return self.filter(id=player_id)

    def get_player_dwithin(self, geom_object, distance):
        return self.filter(location__coordinates__dwithin=(geom_object,
                                                           km_to_degrees(distance)))

    def get_all_player_except_current(self, player_name):
        return self.exclude(user__username=player_name)

    def get_all_player_with_location_except_current(self, player_name):
        return self.exclude(location__exact=None).exclude(user__username=player_name)


class PlayerFollowingQueryset(models.QuerySet):
    def get_player_following(self, follower, following):
        return self.filter(follower=follower, following=following)
