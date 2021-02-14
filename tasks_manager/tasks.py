from celery import shared_task

from core.models.match import Match
from core.models.player import Player
from .email import send_alert_email_for_match

from django.db.models import Case, When
from django.utils import timezone


@shared_task
def update_match_status():

    active_match_qs = Match.objects.get_active_match()

    start_condition_update = When(start_fixture__lte=timezone.now(), then=True)
    over_condition_update = When(end_fixture__lte=timezone.now(), then=True)

    active_match_qs.update(started=Case(start_condition_update, default=False))
    active_match_qs.update(over=Case(over_condition_update, default=False))


@shared_task
def send_alert_email_for_match_task(match_id, distance, host_values):

    match = Match.objects.get_match_by_id(match_id).first()
    player_qs = Player.objects.get_player_dwithin(match, distance)

    recipient_list = [player.user.email for player in player_qs]

    return send_alert_email_for_match(match, recipient_list, host_values)
