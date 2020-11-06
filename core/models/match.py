from django.contrib.gis.db import models

from core.models.location import Location
from core.models.address import Address

class Match(models.Model):

    CLASSIFICATION_CHOICES =  (("Pub", "Public"), ("Priv", "Privé"))

    classification = models.CharField(max_length=255, choices=CLASSIFICATION_CHOICES)
    fixture = models.DateTimeField(auto_now=False, auto_now_add=False)
    num_player = models.IntegerField()
    capacity = models.IntegerField()
    full = models.BooleanField()
    started = models.BooleanField()
    cancelled = models.BooleanField()
    over = models.BooleanField()

    location = models.ForeignKey(Location, on_delete=models.RESTRICT, default=None)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, default=None)