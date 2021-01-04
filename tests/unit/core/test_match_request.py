from django.test import TestCase
from core.models.match_request import MatchRequest
from datetime import datetime
from django.utils.timezone import make_aware


class MatchResquestTest(TestCase):

    fixtures = ["data.json"]

    def test_match_request_instance(self):
        match_request = MatchRequest.objects.get(id=1)
        self.assertEqual(match_request.request_date, make_aware(
            datetime(2020, 1, 1, 1, 0, 0)))
