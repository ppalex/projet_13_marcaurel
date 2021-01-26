from django.db import models

from notifications.querysets.notification_qs import NotificationQuerySet


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def get_notif_for_user(self, id, to_user):
        return self.get_queryset().get_notif_for_user(id=id, to_user=to_user)

    def get_notif_for_user_by_date(self, to_user):
        return self.get_queryset().get_notif_for_user_by_date(to_user=to_user)

    def get_unread_notif_for_user_by_date(self, to_user):
        return self.get_queryset().get_unread_notif_for_user_by_date(to_user=to_user)

    def get_follow_notifications(self, from_user, to_user):
        return self.get_queryset().get_follow_notifications(from_user=from_user,
                                                            to_user=to_user)

    def get_unread_notifications_count(self, to_user):
        return self.get_queryset().get_unread_notifications_count(to_user)
