from django.db import models


class MatchQueryset(models.QuerySet):
    def get_all_match(self):
        return self.all()

    def get_match_by_id(self, match_id):
        return self.filter(id=match_id)

    def count_pending_requests(self, match_id):
        return self.filter(id=match_id, status="pending").count()

    def get_active_match(self):
        return self.filter(cancelled=False, over=False)
