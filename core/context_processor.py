from notifications.models.notification import Notification


def core(request):
    """This function creates a context processor with data needed.

    Args:
        request ([type]): [description]

    Returns:
        [kwargs]: Contains all data stored in the context processor.
    """
    kwargs = {}
    if request.user.is_authenticated:
        kwargs = {
            'notification_count': Notification.objects.get_unread_notifications_count(request.user),
        }
    return kwargs
