from django.contrib.gis.db import models

from core.models.location import Location
from core.models.address import Address
from core.models.player import Player


class Match(models.Model):

    CLASSIFICATION_CHOICES = (("public", "Public"), ("private", "Privé"))

    classification = models.CharField(
        max_length=255, choices=CLASSIFICATION_CHOICES)

    fixture = models.DateTimeField(auto_now=False, auto_now_add=False)
    num_player = models.IntegerField()
    available_place = models.IntegerField()
    capacity = models.IntegerField()
    full = models.BooleanField()
    started = models.BooleanField()
    cancelled = models.BooleanField()
    over = models.BooleanField()

    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, default=None)

    administrator = models.ForeignKey(
        Player, on_delete=models.CASCADE, default=None,
        related_name='administrator')

    players = models.ManyToManyField(Player, through='Registration')
