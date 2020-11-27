from django.contrib.auth import get_user_model

from django.contrib.gis.db import models

from core.models.location import Location
from core.models.address import Address


class Player(models.Model):

    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    player_subscriptions = models.ManyToManyField("self", blank=True,
                                                  symmetrical=False)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
