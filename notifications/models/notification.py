from django.db import models

from users.models.user import User
from models.notification_type import NotificationType


class Notification(models.Model):

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    notification_type = models.OneToOneField(
        NotificationType, on_delete=models.CASCADE)

    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateField(auto_now_add=True)

    is_read = models.BooleanField(default=False)
