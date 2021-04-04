from django.test import TestCase
from tasks_manager.tasks import update_match_status
from core.models.match import Match


class TasksTestCase(TestCase):

    fixtures = ["data.json"]

    def test_update_match_status(self):
        match_before_task = Match.objects.get_match_by_id(4).first()
        update_match_status()
        match_after_task = Match.objects.get_match_by_id(4).first()

        self.assertFalse(match_before_task.over)
        self.assertTrue(match_after_task.over)
