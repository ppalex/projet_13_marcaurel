from django.test import TestCase

from search_manager.utils import km_to_degrees


class UtilsTest(TestCase):

    def test_km_to_degrees(self):

        num_km = 1
        degrees = km_to_degrees(num_km)

        self.assertEqual(degrees, 0.009000000000000001)
