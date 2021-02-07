from django.test import TestCase
from django.urls import reverse
from users.models.user import User


class CreateMatchViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('match-creation'))
        self.assertRedirects(response, '/login/?next=/match/create/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/create/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-creation'))

        self.assertEqual(response.status_code, 200)


class MatchListViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('match-planned'))
        self.assertRedirects(response, '/login/?next=/match/list/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/list/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-planned'))

        self.assertEqual(response.status_code, 200)


class MatchDetailViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/detail/1')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
