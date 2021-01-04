from django.test import TestCase
from core.models.address import Address


class AddressTestCase(TestCase):
    fixtures = ["data.json"]

    def test_address_instance(self):

        address = Address.objects.get(id=1)

        self.assertEqual(address.city, "Bruxelles")
        self.assertEqual(address.street, "rue des bouchers")
        self.assertEqual(address.number, 1)
        self.assertEqual(address.region, "Bruxelles")
