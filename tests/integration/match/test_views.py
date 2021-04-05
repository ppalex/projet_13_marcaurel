from django.test import TestCase
from django.urls import reverse
from users.models.user import User
from core.models.match import Match
from core.models.invitation import Invitation


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


class CancelMatchViewIntegrationTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_match_is_cancelled(self):
        self.client.login(
            username='user1', password='user1')

        match = Match.objects.get_match_by_id(1).first()

        self.client.post(
            reverse('cancel-match', kwargs={"pk": match.id}))

        self.assertFalse(Match.objects.get_match_by_id(1).exists())


class SubscribeInMatchIntegrationTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_player_is_subscribed(self):
        user = User.objects.get(id=1)
        self.client.login(
            username='user1', password='user1')

        match = Match.objects.get(id=3)

        data = {
            'match_id': match.id,
            'action': "S'inscrire"
        }

        self.client.post(
            reverse('match-detail', kwargs={"pk": match.id}), data)

        self.assertTrue(user.player in match.players.all())


class UnsubscribeFromMatchIntegrationTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_player_is_unsubscribed(self):
        user = User.objects.get(id=1)
        self.client.login(
            username='user1', password='user1')

        match = Match.objects.get(id=1)

        data = {
            'match_id': match.id,
            'action': "Se désinscrire"
        }

        self.client.post(
            reverse('match-detail', kwargs={"pk": match.id}), data)

        self.assertTrue(user.player not in match.players.all())


class InvitePlayerInMatchIntegrationTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):

        User.objects.create_user(
            username='user_invited', password='1X<ISRUkw+tuK')

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_player_is_unsubscribed(self):
        user_invited = User.objects.get(username='user_invited')

        self.client.login(
            username='user1', password='user1')

        match = Match.objects.get(id=1)

        data = {
            'form-INITIAL_FORMS': '0',
            'form-TOTAL_FORMS': '1',
            'form-MAX_NUM_FORMS': '',
            'match_id': match.id,
            'form-0-player_name': "user_invited",
            'action': "Inviter"
        }

        self.client.post(
            reverse('match-detail', kwargs={"pk": match.id}), data)

        self.assertTrue(
            Invitation.objects.count_player_pending_invitations(user_invited.id), 1)
