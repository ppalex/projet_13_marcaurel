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


class MatchPlannedViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('match-planned'))
        self.assertRedirects(response, '/login/?next=/match/list/planned')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/list/planned')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-planned'))

        self.assertEqual(response.status_code, 200)


class MatchOverViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('match-over'))
        self.assertRedirects(response, '/login/?next=/match/list/over')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/list/over')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-over'))

        self.assertEqual(response.status_code, 200)


class MatchInProgressViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('match-in-progress'))
        self.assertRedirects(
            response, '/login/?next=/match/list/in-progress')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/list/in-progress')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('match-in-progress'))

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


class MatchSubscriptionListViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/subscription/list/planned')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(
            reverse('match-subscription-planned'))

        self.assertEqual(response.status_code, 200)


class UpdateMatchViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('match/update/1')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(
            reverse('match-update', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)


class KickPlayerViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.post('remove-player/2/')

        self.assertEqual(response.status_code, 200)


class CancelMatchViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.post('cancel-match/1/')

        self.assertEqual(response.status_code, 200)
