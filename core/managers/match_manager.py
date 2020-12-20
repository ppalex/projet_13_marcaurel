from django.db import models

from core.querysets.match_qs import MatchQueryset


class MatchManager(models.Manager):

    def get_queryset(self):
        return MatchQueryset(self.model, using=self._db)

    def get_match_request(self):
        return self.get_queryset().get_match_requests()

    def count_pending_requests(self, match_id):
        return self.get_queryset().count_match_requests(match_id)
