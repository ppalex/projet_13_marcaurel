from django.db import models


class MatchQueryset(models.QuerySet):
    def get_match_requests(self):
        return self.all()

    def count_pending_requests(self, match_id):
        return self.filter(id=match_id, status="pending").count()
