from django.db import models
from .user import User
from datetime import date
from core.models.location import Location
from core.models.address import Address
from core.models.position import Position


class Profile(models.Model):
    SEX_CHOICES = (('masculine', 'M'), ('feminine', 'F'))
    LEVEL_CHOICES = (('novice', 'Débutant'),
                     ('intermediate', 'Intermédiaire'),
                     ('advanced', 'Avancé'))

    firstname = models.CharField(max_length=255, null=True,
                                 blank=True)

    name = models.CharField(max_length=255, null=True,
                            blank=True)

    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True)

    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True,
                           blank=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, null=True,
                             blank=True)

    address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, null=True, blank=True)

    positions = models.ManyToManyField(Position, default=None, null=True,
                                       blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'

    def get_age(self):
        today = date.today()
        born = self.birthdate
        if born:
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        else:
            return 0

    def get_level(self):
        return f"{self.get_level_display()}"
