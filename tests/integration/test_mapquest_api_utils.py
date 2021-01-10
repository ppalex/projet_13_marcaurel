from django.test import TestCase

from api_manager.models.mapquest_api import MapquestApi
from api_manager.utils.mapquest_utils import get_address_coordinates
from unittest import mock


class MapquestApiUtilsTestCase(TestCase):

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

        coordinates = get_address_coordinates(
            street="Rue des Anglais",
            number='12',
            city='Jurbise',
            region='mons'
        )
        self.assertEqual(coordinates, (50.53162, 3.908024))
