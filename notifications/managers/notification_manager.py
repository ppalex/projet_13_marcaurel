from django.db import models

from notifications.querysets.notification_qs import NotificationQuerySet


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def get_notif_for_user(self, id, to_user):
        return self.get_queryset().get_notif_for_user(id=id, to_user=to_user)

    def get_notif_for_user_by_date(self, to_user):
        return self.get_queryset().get_notif_for_user_by_date(to_user=to_user)

    def get_follow_notifications(self, follower, following):
        return self.get_queryset().get_notif_for_user_by_date(from_user=follower,
                                                              to_user=following)
