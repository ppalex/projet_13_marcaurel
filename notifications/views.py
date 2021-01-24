from django.views.generic.list import ListView

from .models.notification import Notification


class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
