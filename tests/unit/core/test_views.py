from django.test import TestCase
from django.urls import reverse
from users.models.user import User


class IndexViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/login/?next=/index/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('/index/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)


class LandingViewTest(TestCase):

    fixtures = ["data.json"]

    def test_view_url_exists_at_desired_location(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):

        response = self.client.get(reverse('landing'))

        self.assertEqual(response.status_code, 200)


class LegalViewTest(TestCase):

    fixtures = ["data.json"]

    def test_view_url_exists_at_desired_location(self):

        response = self.client.get('/legal/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):

        response = self.client.get(reverse('legal'))

        self.assertEqual(response.status_code, 200)
