from django.test import TestCase
from core.models.player import Player
from core.models.address import Address
from core.models.position import Position


class PlayerTestCase(TestCase):

    fixtures = ["data.json"]

    def test_player_instance(self):
        player = Player.objects.get(firstname='user1_firstname')

        self.assertEqual(player.firstname, "user1_firstname")
        self.assertIsInstance(player.address, Address)
        self.assertIsInstance(player.position.first(), Position)
