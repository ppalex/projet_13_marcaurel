from django.db import models


class RegistrationQuerySet(models.QuerySet):

    def get_registration(self, id):
        return self.filter(id=id)

    def create_registration(self, **kwargs):
        registration = self.model(**kwargs)
        registration.save()

        return registration
