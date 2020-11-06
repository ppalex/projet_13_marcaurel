from django.contrib.gis.db import models

from core.models.location import Location
from core.models.address import Address

class Player(models.Model):

    SEX_CHOICES = (('Masculin', 'M'),('Féminin', 'F'))
    LEVEL_CHOICES = (('D', 'Débutant'), ('I', 'Intermédiaire'), ('A', 'Avancé'))

    player_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)

    location = models.ForeignKey(Location, on_delete=models.RESTRICT, default=None)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, default=None)

    def __str__(self):
        return f"{self.firstname} {self.name}"
