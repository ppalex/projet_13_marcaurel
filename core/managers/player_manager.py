from django.db import models

from core.querysets.player_qs import PlayerQueryset, PlayerSubscriptionQueryset


class PlayerManager(models.Manager):
    def get_queryset(self):
        return PlayerQueryset(self.model, using=self._db)

    def get_player_name_start_with(self, term):
        return self.get_queryset().get_player_name_start_with(term)

    def get_player(self, player_name):
        return self.get_queryset().get_player(player_name)

    def get_player_by_id(self, player_id):
        return self.get_queryset().get_player_by_id(player_id)

    def get_player_dwithin(self, geom_object, distance):
        return self.get_queryset().get_player_dwithin(
            geom_object.location.coordinates, distance)

    def get_all_player_except_current(self, player_name):
        return self.get_queryset().get_all_player_except_current(player_name)

    def get_all_player_with_location_except_current(self, player_name):
        return self.get_queryset().get_all_player_with_location_except_current(player_name)


class PlayerSubscriptionManager(models.Manager):

    def get_queryset(self):
        return PlayerSubscriptionQueryset(self.model, using=self._db)

    def get_player_following(self, follower, following):
        return self.get_queryset().get_player_following(follower, following)
