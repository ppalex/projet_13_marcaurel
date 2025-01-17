from django.test import TestCase
from core.models.match import Match


class MatchTestCase(TestCase):

    fixtures = ["data.json"]

    def test_match_instance(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        self.assertEqual(match.classification, 'private')

    def test_match_administrator_relationship(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        self.assertEqual(match.administrator.user.profile.firstname, 'user1_firstname')

    def test_match_player_relationship(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        players = match.players.all()
        player = players[1]

        self.assertEqual(player.user.profile.firstname, 'user2_firstname')
