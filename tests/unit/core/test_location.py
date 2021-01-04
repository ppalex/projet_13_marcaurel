from django.test import TestCase
from core.models.location import Location

from django.contrib.gis.geos import Point


class LocationTestCase(TestCase):

    def setUp(self):

        longitude = 50
        latitude = 50

        Location.objects.create(
            coordinates=Point(longitude, latitude, srid=4326)
        )

    def test_location_instance(self):
        location = Location.objects.get(id=1)

        self.assertEqual(location.coordinates.x, 50)
        self.assertEqual(location.coordinates.y, 50)
