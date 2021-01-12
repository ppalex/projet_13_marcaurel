from django.test import TestCase
from django.urls import reverse
from users.models.user import User


class SearchMapMatchViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('search-map-match'))
        self.assertRedirects(response, '/login/?next=/search/map/match/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get('search/map/match/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse('search-map-match'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse('search-map-match'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'search_manager/search_map_match.html')


class SearchTableMatchViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('search-table-match'))
        self.assertRedirects(response, '/login/?next=/search/table/match/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get('search/table/match/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse('search-table-match'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse('search-table-match'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'search_manager/search_table_match.html')
