from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models.notification import Notification
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notifications.html'

    def get_queryset(self):
        return Notification.objects.filter(to_user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def delete_notification(request, pk):
    notification = Notification.objects.filter(
        id=pk, to_user=request.user)

    notification.delete()

    return redirect("notifications")
