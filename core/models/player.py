from django.contrib.auth import get_user_model

from django.contrib.gis.db import models

from core.models.location import Location

from django.contrib.gis.geos import Point

from core.managers.player_manager import (
    PlayerManager, PlayerSubscriptionManager)


class Player(models.Model):

    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    player_subscriptions = models.ManyToManyField("self", through="PlayerSubscription", blank=True,
                                                  symmetrical=False)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    objects = PlayerManager()

    def update_location(self, latitude, longitude):

        location = Location.objects.get_or_create(coordinates=Point(
            float(longitude), float(latitude),  srid=4326))

        self.location = location[0]
        self.save()

    def get_followers_count(self):
        return self.following.count()

    def get_followings_count(self):
        return self.follower.count()



class PlayerSubscription(models.Model):
    follower = models.ForeignKey(
        Player, related_name="follower", on_delete=models.CASCADE, default=None)

    following = models.ForeignKey(
        Player, related_name="following", on_delete=models.CASCADE, default=None)

    created = models.DateTimeField(auto_now_add=True)

    objects = PlayerSubscriptionManager()
