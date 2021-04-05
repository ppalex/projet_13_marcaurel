from datetime import date

from django.test import TestCase
from django.urls import reverse

from users.models.user import User


class UserSettingsViewIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_profile_update(self):
        self.client.login(
            username='user1', password='user1')

        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles',
            'firstname': 'Marc',
            'name': 'Aurele',
            'sex': 'masculine',
            'level': '',
            'positions': [],
            'birthdate': '2000-01-01'

        }

        self.client.post(reverse('settings-profile'), data)

        user = User.objects.get(username='user1')
        self.assertEqual(user.profile.firstname, 'Marc')
        self.assertEqual(user.profile.name, 'Aurele')
        self.assertEqual(user.profile.sex, 'masculine')
        self.assertEqual(user.profile.birthdate, date(2000, 1, 1))
