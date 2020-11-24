from django.db import models
from .user import User


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
        Address, on_delete=models.RESTRICT, default=None, null=True,
        blank=True)

    positions = models.ManyToManyField(Position)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
