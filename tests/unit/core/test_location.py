from django.test import TestCase
from core.models.location import Location


class LocationTestCase(TestCase):

    fixtures = ["data.json"]

    def test_location_instance(self):
        location = Location.objects.get(id=1)

        self.assertEqual(location.coordinates.x, 30)
        self.assertEqual(location.coordinates.y, 10)
