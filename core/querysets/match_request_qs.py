from django.db import models


class MatchRequestQueryset(models.QuerySet):
    def get_match_requests(self, match_id):
        return self.filter(for_match=match_id)

    def get_match_request_by_id(self, request_id):
        return self.get(id=request_id)

    def get_pending_requests(self, match_id):
        return self.filter(status="pending", for_match=match_id)

    def count_pending_requests(self, match_id):
        return self.get_pending_requests(match_id).count()

    def get_request(self, request_id):
        return self.filter(id=request_id)

    def get_by_player(self):
        return self.by_player

    def count_player_pending_requests(self, player):
        return self.filter(status='pending', by_player=player).count()

    def get_player_pending_requests(self, player):
        return self.filter(status='pending', by_player=player)

    def get_existing_request_by_player_match_status(self, status, by_player, for_match):
        return self.filter(status='pending', by_player=by_player, for_match=for_match).exists()
