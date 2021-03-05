from django.db import models

from core.querysets.match_qs import MatchQueryset


class MatchManager(models.Manager):

    def get_queryset(self):
        return MatchQueryset(self.model, using=self._db)

    def get_all_match(self):
        return self.get_queryset().get_all_match()

    def get_match_by_id(self, match_id):
        return self.get_queryset().get_match_by_id(match_id)

    def count_pending_requests(self, match_id):
        return self.get_queryset().count_match_requests(match_id)

    def get_active_match(self):
        return self.get_queryset().get_active_match()

    def get_planned_match(self, administrator):
        return self.get_queryset().get_planned_match(administrator)

    def get_in_progress_match(self, administrator):
        return self.get_queryset().get_in_progress_match(administrator)

    def get_over_match(self, administrator):
        return self.get_queryset().get_over_match(administrator)
