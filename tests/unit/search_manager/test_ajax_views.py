from django.test import RequestFactory, TestCase
from search_manager.ajax_view import (filter_match_view, autocomplete_city,
                                      autocomplete_player)
from users.models.user import User
import json
import pdb


class FilterMatchView(TestCase):
    fixtures = ["data.json"]

    @classmethod
    def setUpTestData(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username='user3', email='user3@gmail.com', password='password')

    def test_classification_filter(self):
        self.client.login(username='user3', password='password')
        data = {'classification': 'public',
                'city': '',
                'available_place': '',
                'start_fixture': '',
                'location': '',
                }

        request = self.factory.post('/search/match/filter', data)

        request.user = self.user

        response = filter_match_view(request)
        json_response = json.loads(response.content)
        match = json_response[0]
        self.assertEqual(match['classification'], 'public')


class AutocompleteCityTest(TestCase):

    fixtures = ["data.json"]

    @classmethod
    def setUpTestData(self):
        self.factory = RequestFactory()

    def test_autocomplete(self):
        data = {'term': 'B'}
        request = self.factory.get('/autocomplete', data)

        json_response = autocomplete_city(request)

        self.assertJSONEqual(
            str(json_response.content, encoding='utf8'),
            ['Bruxelles']
        )


class AutocompletePlayerTest(TestCase):

    fixtures = ["data.json"]

    @classmethod
    def setUpTestData(self):
        self.factory = RequestFactory()

    def test_autocomplete(self):
        data = {'term': 'u'}
        request = self.factory.get('/autocomplete', data)

        json_response = autocomplete_player(request)

        self.assertJSONEqual(
            str(json_response.content, encoding='utf8'),
            ['user1', 'user2']
        )
