from notifications.models.notification import Notification
from core.models.invitation import Invitation
from core.models.match_request import MatchRequest


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
            'invitations_count_current_player': Invitation.objects.count_player_pending_invitations(request.user.player),
            'invitations_current_player': Invitation.objects.get_player_pending_invitations(request.user.player),
            'requests_count_current_player': MatchRequest.objects.count_player_pending_requests(request.user.player),
            'requests_current_player': MatchRequest.objects.get_player_pending_requests(request.user.player)
        }
    return kwargs
