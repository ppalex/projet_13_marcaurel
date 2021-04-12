from django.db import models

from core.querysets.registration_qs import RegistrationQuerySet


class RegistrationManager(models.Manager):
    def get_queryset(self):
        return RegistrationQuerySet(self.model, using=self._db)

    def get_registration(self, id):
        return self.get_queryset().get_registration(id)

    def get_opened_registration_for_player(self, player):
        return self.get_queryset().get_opened_registration_for_player(player)

    def create_registration(self, **kwargs):
        return RegistrationQuerySet.create_registration(**kwargs)
