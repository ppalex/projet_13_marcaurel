from django.test import TestCase, override_settings
from tasks_manager.tasks import update_match_status


class TasksTestCase(TestCase):

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_update_match_status(self):
        self.assertTrue(update_match_status.delay())
