from django.db import models


class NotificationType(models.Model):
    NOTIFICATIONS_TYPE = ((1, 'invitation-accepted'),
                          (2, 'invitation-refused'),
                          (3, 'follow'))

    notification_type = models.IntegerField(choices=NOTIFICATIONS_TYPE)
