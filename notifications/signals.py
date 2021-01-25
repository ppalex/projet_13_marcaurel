from django.db.models.signals import post_save, post_delete
from core.models.player import PlayerSubscription
from .models.notification import Notification
from django.dispatch import receiver


@receiver(post_save, sender=PlayerSubscription)
def user_follow(sender, instance, created, **kwargs):
    if created:
        player_sub = instance
        follower = player_sub.follower.user
        following = player_sub.following.user

        Notification.objects.create(
            from_user=follower,
            to_user=following,
            notification_type=3)


@receiver(post_delete, sender=PlayerSubscription)
def user_unfollow(sender, instance, *args, **kwargs):
    player_sub = instance
    follower = player_sub.follower.user
    following = player_sub.following.user
    
    notify = Notification.objects.get_follow_notifications(
        from_user=follower,
        to_user=following)

    notify.delete()
