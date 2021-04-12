from django.db import models


class MatchQueryset(models.QuerySet):
    def get_all_match(self):
        """This method gets all matchs.

        Returns:
            Queryset: contains all the matchs.
        """
        return self.all()

    def get_match_by_id(self, match_id):
        return self.filter(id=match_id)

    def count_pending_requests(self, match_id):
        """This method counts all pending for a match by ID.

        Returns:
            Queryset: contains all pending requests for a match.
        """
        return self.filter(id=match_id, status="pending").count()

    def get_active_match(self):
        """This method gets actives matchs.

        Returns:
            Queryset: contains all actives matchs.
        """
        return self.filter(cancelled=False, over=False)

    def get_planned_match(self, administrator):
        """This method gets all planned matchs for administrator player.

        Returns:
            Queryset: contains all planned matchs.
        """
        return self.filter(administrator=administrator, started=False,
                           over=False)

    def get_in_progress_match(self, administrator):
        """This method gets all matchs in progress for administrator player.

        Returns:
            Queryset: contains all the matchs.
        """
        return self.filter(administrator=administrator, started=True,
                           over=False)

    def get_over_match(self, administrator):
        """This method gets all overed matchs for administrator player.

        Returns:
            Queryset: contains all overed matchs.
        """
        return self.filter(administrator=administrator, over=True)

    def get_planned_match_subscription(self, administrator):
        return self.filter(started=False, over=False).exclude(
            administrator=administrator)

    def get_in_progress_match_subscription(self, administrator):
        return self.filter(started=True, over=False).exclude(
            administrator=administrator)

    def get_over_match_subscription(self, administrator):
        return self.filter(over=True).exclude(
            administrator=administrator)
