from django.db import models
from core.querysets.player_qs import PlayerQueryset


class PlayerManager(models.Manager):
    def get_queryset(self):
        return PlayerQueryset(self.model, using=self._db)

    def get_player_name_start_with(self, term):
        return self.get_queryset().get_player_name_start_with(term)
