from django.db.models.signals import post_save
from .models.user import User
from django.dispatch import receiver
from .models.profile import Profile

from core.models.player import Player


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwnargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        Player.objects.create(user=instance)
