from django.contrib.gis.db import models

from core.models.location import Location
from core.models.address import Address
from core.models.position import Position


class Player(models.Model):

    SEX_CHOICES = (('masculine', 'M'), ('feminine', 'F'))
    LEVEL_CHOICES = (('novice', 'Débutant'),
                     ('intermediate', 'Intermédiaire'),
                     ('advanced', 'Avancé'))

    firstname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)

    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, default=None)

    position = models.ManyToManyField(Position)
    player_subscription = models.ManyToManyField("self", blank=True,
                                                 symmetrical=False)

    def __str__(self):
        return f"{self.firstname} {self.name}"
