from django.test import TestCase
from core.models.registration import Registration

from datetime import datetime
from django.utils.timezone import make_aware


class RegistrationTest(TestCase):
    fixtures = ["data.json"]

    def test_registration_instance(self):

        registration = Registration.objects.get(id=1)
        self.assertEqual(registration.join_date, make_aware(
            datetime(2020, 1, 1, 1, 0, 0)))

    def test_registration_relationship(self):
        registration = Registration.objects.get(id=1)

        self.assertEqual(registration.player.user.profile.firstname, 'user2_firstname')
        self.assertEqual(registration.match.id, 1)
