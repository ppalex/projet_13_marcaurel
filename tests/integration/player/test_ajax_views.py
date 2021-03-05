from django.test import TestCase
from django.urls import reverse
from users.models.user import User


class PlayerFollowingIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_player_follow(self):
        self.client.login(
            username='user1', password='user1')

        user_1 = User.objects.get(id=1)
        user_2 = User.objects.get(id=2)

        data = {
            'player_id': "2",
            'action': "follow"
        }
        self.client.post(
            reverse('player-follow'), data)

        self.assertTrue(
            user_2.player in user_1.player.player_subscriptions.all())
        self.assertEqual(user_2.player.get_followers_count(), 1)

    def test_player_unfollow(self):
        self.client.login(
            username='user2', password='user2')

        user_1 = User.objects.get(id=1)
        user_2 = User.objects.get(id=2)

        data = {
            'player_id': "1",
            'action': "unfollow"
        }
        self.client.post(
            reverse('player-follow'), data)

        self.assertFalse(
            user_1.player in user_2.player.player_subscriptions.all())
        self.assertEqual(user_2.player.get_followers_count(), 0)
