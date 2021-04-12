from django.db import models

from core.querysets.match_qs import MatchQueryset


class MatchManager(models.Manager):

    def get_queryset(self):
        """This method return the queryset of the Match model.

        Returns:
            Queryset: contains all the querysets method for Match object.
        """
        return MatchQueryset(self.model, using=self._db)

    def get_all_match(self):
        """This method gets all matchs.

        Returns:
            Queryset: contains all the matchs.
        """
        return self.get_queryset().get_all_match()

    def get_match_by_id(self, match_id):
        """This method gets all matchs by match ID.

        Returns:
            Queryset: contains all the matchs.
        """
        return self.get_queryset().get_match_by_id(match_id)

    def count_pending_requests(self, match_id):
        """This method counts all pending for a match by ID.

        Returns:
            Queryset: contains all pending requests for a match.
        """
        return self.get_queryset().count_pending_requests(match_id)

    def get_active_match(self):
        """This method gets actives matchs.

        Returns:
            Queryset: contains all actives matchs.
        """
        return self.get_queryset().get_active_match()

    def get_planned_match(self, administrator):
        """This method gets all planned matchs for administrator player.

        Returns:
            Queryset: contains all planned matchs.
        """
        return self.get_queryset().get_planned_match(administrator)

    def get_in_progress_match(self, administrator):
        """This method gets all matchs in progress for administrator player.

        Returns:
            Queryset: contains all the matchs.
        """
        return self.get_queryset().get_in_progress_match(administrator)

    def get_over_match(self, administrator):
        """This method gets all overed matchs for administrator player.

        Returns:
            Queryset: contains all overed matchs.
        """
        return self.get_queryset().get_over_match(administrator)

    def get_planned_match_subscription(self, administrator):
        return self.get_queryset().get_planned_match_subscription(
            administrator)

    def get_in_progress_match_subscription(self, administrator):
        return self.get_queryset().get_in_progress_match_subscription(
            administrator)

    def get_over_match_subscription(self, administrator):
        return self.get_queryset().get_over_match_subscription(administrator)
