from celery import shared_task

from core.models.match import Match


from django.db.models import Case, When
from django.utils import timezone


@shared_task
def update_match_status():

    active_match_qs = Match.objects.get_active_match()

    start_condition_update = When(start_fixture__lte=timezone.now(), then=True)
    over_condition_update = When(end_fixture__lte=timezone.now(), then=True)

    active_match_qs.update(started=Case(start_condition_update, default=False))
    active_match_qs.update(over=Case(over_condition_update, default=False))
