from django.test import TestCase
import requests
from api_manager.models.mapquest_api import MapquestApi
from unittest import mock


class MapquestApiTestCase(TestCase):

    @mock.patch('api_manager.models.mapquest_api.requests.get')
    def test_send_request(self, mock_get):

        results = {
            "results": [
                {
                    "locations": [
                        {
                            "street": "Rue des Anglais",
                            "adminArea5": "Jurbise",
                            "adminArea5Type": "City",
                            "adminArea4": "Mons",
                            "adminArea3": "Wallonia",
                            "postalCode": "7050",
                            "latLng": {
                                "lat": 50.53162,
                                "lng": 3.908024
                            }
                        }
                    ]
                }
            ]
        }
        mock_get().status_code = 200
        mock_get().json.return_value = results

        mapquest = MapquestApi()
        mapquest.send_request(
            street="Rue des Anglais",
            number='12',
            city='Jurbise',
            region='mons'
        )
        self.assertEqual(mapquest.get_data(), results)
        self.assertEqual(mapquest.get_latitude(), 50.53162)
        self.assertEqual(mapquest.get_longitude(), 3.908024)

    def test_api_timeout_exception(self):

        with mock.patch('api_manager.models.mapquest_api.requests.get') as mock_requests:
            mock_requests.side_effect = requests.exceptions.Timeout(
                'Timeout error')

            mapquest = MapquestApi()

            with self.assertRaises(SystemExit) as cm:

                response = mapquest.send_request(
                    street="Rue des Anglais",
                    number='12',
                    city='Jurbise',
                    region='mons'
                )

                self.assertTrue(response is None)
        self.assertTrue(isinstance(cm.exception, SystemExit))
        self.assertEqual(str(cm.exception.code), 'Timeout error')

    def test_api_redirects_exception(self):

        with mock.patch('api_manager.models.mapquest_api.requests.get') as mock_requests:
            mock_requests.side_effect = requests.exceptions.TooManyRedirects(
                'Bad url')

            mapquest = MapquestApi()

            with self.assertRaises(SystemExit) as cm:

                response = mapquest.send_request(
                    street="Rue des Anglais",
                    number='12',
                    city='Jurbise',
                    region='mons'
                )

                self.assertTrue(response is None)
        self.assertTrue(isinstance(cm.exception, SystemExit))
        self.assertEqual(str(cm.exception.code), 'Bad url')

    def test_api_request_exception(self):

        with mock.patch('api_manager.models.mapquest_api.requests.get') as mock_requests:
            mock_requests.side_effect = requests.exceptions.RequestException(
                'Bad request')

            mapquest = MapquestApi()

            with self.assertRaises(SystemExit) as cm:

                response = mapquest.send_request(
                    street="Rue des Anglais",
                    number='12',
                    city='Jurbise',
                    region='mons'
                )

                self.assertTrue(response is None)
        self.assertTrue(isinstance(cm.exception, SystemExit))
        self.assertEqual(str(cm.exception.code), 'Bad request')

    @mock.patch('api_manager.models.mapquest_api.requests.get')
    def test_api_get_latitude_exception(self, mock_get):
        results = {
            "results": [
                {
                    "locations": [
                        {
                            "street": "Rue des Anglais",
                            "adminArea5": "Jurbise",
                            "adminArea5Type": "City",
                            "adminArea4": "Mons",
                            "adminArea3": "Wallonia",
                            "postalCode": "7050",
                            "latLng": {
                                "latitude": 50.53162,
                                "longitude": 3.908024
                            }
                        }
                    ]
                }
            ]
        }
        mock_get().status_code = 200
        mock_get().json.return_value = results

        mapquest = MapquestApi()

        mapquest.send_request(
            street="Rue des Anglais",
            number='12',
            city='Jurbise',
            region='mons'
        )

        with self.assertRaises(KeyError) as cm:
            mapquest.get_latitude()

    @mock.patch('api_manager.models.mapquest_api.requests.get')
    def test_api_get_longitude_exception(self, mock_get):
        results = {
            "results": [
                {
                    "locations": [
                        {
                            "street": "Rue des Anglais",
                            "adminArea5": "Jurbise",
                            "adminArea5Type": "City",
                            "adminArea4": "Mons",
                            "adminArea3": "Wallonia",
                            "postalCode": "7050",
                            "latLng": {
                                "latitude": 50.53162,
                                "longitude": 3.908024
                            }
                        }
                    ]
                }
            ]
        }
        mock_get().status_code = 200
        mock_get().json.return_value = results

        mapquest = MapquestApi()

        mapquest.send_request(
            street="Rue des Anglais",
            number='12',
            city='Jurbise',
            region='mons'
        )

        with self.assertRaises(KeyError) as cm:
            mapquest.get_longitude()
