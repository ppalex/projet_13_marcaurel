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
        """ This method checks if a player plays in a match.

        Args:
            player (Player): Player object.

        Returns:
            Boolean: True if the player is in the match.
        """
        if self.players.filter(id=player.id).exists():
            return True
        else:
            return False

    def is_full(self):
        """ This method check the match is full.

        Returns:
            Boolean: True if full.
        """
        return self.full

    def is_over(self):
        """ This method check the match is over.

        Returns:
            Boolean: True if over.
        """
        return self.over

    def is_started(self):
        """This method check the match is started.

        Returns:
            Boolean: True if started.
        """
        return self.started

    def add_player(self):
        """ This method add a player to a match.
        """
        if not self.is_full():
            self.num_player += 1
            self.available_place -= 1
            self.update_full_status()
            self.save()

    def remove_player(self):
        """ This method remove a player from a match.
        """
        if self.num_player > 0:
            self.num_player -= 1
            self.available_place += 1
            self.update_full_status()
            self.save()

    def update_full_status(self):
        """ This update de status of a match if the match is full.
        """
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
