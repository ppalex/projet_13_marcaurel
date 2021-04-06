
from django.test import TestCase
from core.models.registration import Registration


class RegistrationManagerTest(TestCase):
    fixtures = ["data.json"]

    def test_registration_manager(self):
        registration = Registration.objects.get_registration(id=2)

        self.assertTrue(registration.exists())
        self.assertEqual(registration.first().id, 2)
