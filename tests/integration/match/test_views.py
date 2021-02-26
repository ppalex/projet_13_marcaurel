from django.test import TestCase
from django.urls import reverse
from users.models.user import User
from core.models.match import Match


class KickPlayerViewIntegrationTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_player_is_kicked(self):
        self.client.login(
            username='user1', password='user1')

        user = User.objects.get(id=2)
        match = Match.objects.get(id=1)

        num_player = match.num_player
        available_place = match.available_place

        data = {
            'player_id': user.player.id
        }
        self.client.post(
            reverse('remove-player', kwargs={"pk": match.id}), data)
        match = Match.objects.get(id=1)

        self.assertEqual(user.player in match.players.all(), False)
        self.assertEqual(match.num_player, num_player-1)
        self.assertEqual(match.available_place, available_place+1)
