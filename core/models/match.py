from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from core.managers.match_manager import MatchManager
from core.models.address import Address
from core.models.location import Location
from core.models.player import Player


class Match(models.Model):

    CLASSIFICATION_CHOICES = (("public", "Public"), ("private", "Privé"))

    classification = models.CharField(
        max_length=255, choices=CLASSIFICATION_CHOICES)

    start_fixture = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_fixture = models.DateTimeField(auto_now=False, auto_now_add=False)
    num_player = models.IntegerField()
    available_place = models.IntegerField()
    capacity = models.IntegerField()
    full = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    over = models.BooleanField(default=False)

    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, default=None)

    administrator = models.ForeignKey(
        Player, on_delete=models.CASCADE, default=None,
        related_name='administrator')

    players = models.ManyToManyField(Player, through='Registration')

    objects = MatchManager()

    def match_has_player(self, player):
        if self.players.filter(id=player.id).exists():
            return True
        else:
            return False

    def is_full(self):
        return self.full

    def is_over(self):
        return self.over

    def is_started(self):
        return self.started

    def add_player(self):
        if not self.is_full():
            self.num_player += 1
            self.available_place -= 1
            self.update_full_status()
            self.save()

    def remove_player(self):
        if self.num_player > 0:
            self.num_player -= 1
            self.available_place += 1
            self.update_full_status()
            self.save()

    def update_full_status(self):
        if self.num_player == self.capacity:
            self.full = True
        else:
            self.full = False

    def cancel(self):
        self.delete()

    def set_location(self, latitude, longitude):
        match_location = Location.objects.create(
            coordinates=Point(longitude, latitude, srid=4326)
        )
        self.location = match_location
