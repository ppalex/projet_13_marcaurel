from django.test import TestCase

from datetime import date
from django.contrib.gis.geos import Point

from core.models.address import Address
from core.models.player import Player


class AddressTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            city="Bruxelles",
            street="rue des bouchers",
            number=1,
            region="Bruxelles"
        )

    def test_address_instance(self):

        address = Address.objects.get(id=1)

        self.assertEqual(address.city, "Bruxelles")
        self.assertEqual(address.street, "rue des bouchers")
        self.assertEqual(address.number, 1)
        self.assertEqual(address.region, "Bruxelles")


class PlayerTestCase(TestCase):

    def setUp(self):
        pass

        # Player.objects.create(
        #     firstname="user1_firstname",
        #     name='user1_name',
        #     birthdate=date(2020, 1, 1),
        #     sex='masculine',
        #     level='novice',
        #     location=Point(50, 50),
        #     address=,
        #     position='keeper',
        # )

    def test_player_instance(self):
        pass
