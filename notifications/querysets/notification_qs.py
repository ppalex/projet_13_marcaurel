from django.db import models


class NotificationQuerySet(models.QuerySet):

    def get_notif_for_user(self, id, to_user):
        return self.filter(id=id, to_user=to_user)

    def get_notif_for_user_by_date(self, to_user):
        return self.filter(to_user=to_user).order_by('-date')

    def get_follow_notifications(self, follower, following):
        return self.filter(from_user=follower,
                           to_user=following,
                           notification_type=3)
