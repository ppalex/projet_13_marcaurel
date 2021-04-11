from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from core.models.invitation import Invitation
from core.models.player import PlayerSubscription

from .models.notification import Notification


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


@receiver(post_save, sender=Invitation)
def user_invite(sender, instance, created, **kwargs):
    if created:
        invitation = instance
        from_user = invitation.by_player.user
        to_user = invitation.for_player.user

        Notification.objects.create(
            from_user=from_user,
            to_user=to_user,
            notification_type=1)


# @receiver(post_save, sender=Invitation.accept)
# def user_accept_invitation(sender, instance, created, **kwargs):
#     print("ok")
#     invitation = instance
#     from_user = invitation.for_player.user
#     to_user = invitation.by_player.user

#     Notification.objects.create(
#         from_user=from_user,
#         to_user=to_user,
#         notification_type=2)
