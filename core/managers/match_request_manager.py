from django.db import models

from core.querysets.match_request_qs import MatchRequestQueryset


class MatchRequestManager(models.Manager):

    def get_queryset(self):
        return MatchRequestQueryset(self.model, using=self._db)

    def get_match_request_by_id(self, request_id):
        return self.get_queryset().get_match_request_by_id(request_id)

    def get_match_request(self, match_id):
        return self.get_queryset().get_match_requests(match_id)

    def get_request(self, request_id):
        return self.get_queryset().get_request(request_id)

    def get_pending_requests(self, match_id):
        return self.get_queryset().get_pending_requests(match_id)

    def count_pending_requests(self, match_id):
        return self.get_queryset().count_pending_requests(match_id)

    def count_player_pending_requests(self, player):
        return self.get_queryset().count_player_pending_requests(player)

    def get_player_pending_requests(self, player):
        return self.get_queryset().get_player_pending_requests(player)

    def check_exist_request(self, status, by_player, for_match):

        match_request = self.get_queryset(
        ).get_existing_request_by_player_match_status(status, by_player, for_match)

        if match_request:
            return True
        else:
            return False
