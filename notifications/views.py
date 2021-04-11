from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.list import ListView

from .models.notification import Notification


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notifications.html'

    def get_queryset(self):

        notifications_qs = Notification.objects.get_notif_for_user_by_date(
            self.request.user)

        notifications_qs.update(is_read=True)

        return notifications_qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


@login_required
def delete_notification(request, pk):
    notification = Notification.objects.get_notif_for_user(
        id=pk, to_user=request.user)

    notification.delete()

    return redirect("notifications")
