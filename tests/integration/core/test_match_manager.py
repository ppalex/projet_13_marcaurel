
from django.test import TestCase
from core.models.match import Match


class MatchIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def test_match_manager(self):
        match = Match.objects.get_match_by_id(1)

        all_match = Match.objects.get_all_match()
        active_match = Match.objects.get_active_match()
        planned_match = Match.objects.get_planned_match(administrator=1)

        self.assertTrue(match.exists())
        self.assertEqual(match.first().id, 1)
        self.assertTrue(active_match.count(), 2)
        self.assertTrue(all_match.count(), 3)
        self.assertTrue(planned_match.first().id, 1)
