from django.test import TestCase
from core.models.player import Player


class PlayerTestCase(TestCase):

    fixtures = ["data.json"]

    def test_player_instance(self):
        player = Player.objects.get(id=1)
        self.assertIsInstance(player, Player)
