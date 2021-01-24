from django.contrib import admin

from notifications.models.notification import Notification
from notifications.models.notification_type import NotificationType

admin.site.register(Notification)
admin.site.register(NotificationType)
