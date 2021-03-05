from django.test import TestCase

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
