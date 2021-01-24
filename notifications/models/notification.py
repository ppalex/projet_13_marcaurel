from django.db import models

from users.models.user import User
from notifications.models.notification_type import NotificationType


class Notification(models.Model):

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='noti_from_user', blank=True, default=None)
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='noti_to_user', blank=True,  default=None)

    notification_type = models.OneToOneField(
        NotificationType, on_delete=models.CASCADE)

    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)
