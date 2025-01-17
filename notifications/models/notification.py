from django.db import models

from notifications.managers.notification_manager import NotificationManager
from users.models.user import User


class Notification(models.Model):

    NOTIFICATIONS_TYPE = ((1, 'invitation-send'),
                          (2, 'invitation-accepted'),
                          (3, 'follow'))

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='noti_from_user', blank=True, default=None)
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='noti_to_user', blank=True,  default=None)

    notification_type = models.IntegerField(choices=NOTIFICATIONS_TYPE)

    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    objects = NotificationManager()
