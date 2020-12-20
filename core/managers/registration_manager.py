from django.db import models

from core.querysets.registration_qs import RegistrationQuerySet


class RegistrationManager(models.Manager):
    def get_queryset(self):
        return RegistrationQuerySet(self.model, using=self._db)

    def get_registration(self, id):
        return self.get_queryset().get_registration(id)

    def create_registration(self, **kwargs):
        return RegistrationQuerySet.create_registration(**kwargs)
