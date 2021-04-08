from django.db import models


class RegistrationQuerySet(models.QuerySet):

    def get_registration(self, id):
        return self.filter(id=id)

    def create_registration(self, **kwargs):
        registration = self.model(**kwargs)
        registration.save()

        return registration

    def get_opened_registration_for_player(self, player):
        return self.filter(status='opened', player=player)
