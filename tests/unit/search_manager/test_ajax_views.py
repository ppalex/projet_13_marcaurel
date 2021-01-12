from django.test import RequestFactory, TestCase
from search_manager.ajax_view import (autocomplete_city,
                                      autocomplete_player)


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
