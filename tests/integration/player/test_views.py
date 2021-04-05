from django.test import TestCase
from django.urls import reverse

from core.models.match_request import MatchRequest
from core.models.invitation import Invitation
from users.models.user import User
from core.models.match import Match


class CancelMatchRequestIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_get_request_is_cancelled(self):
        pk = 1
        match_request = MatchRequest.objects.get_match_request_by_id(pk)

        self.assertTrue(isinstance(match_request, MatchRequest))

    def test_match_request_is_cancelled(self):
        self.client.login(
            username='user1', password='user1')

        self.client.post(
            reverse('cancel-match-request', kwargs={'pk': 1}))

        self.assertFalse(MatchRequest.objects.filter(pk=1).exists())


class DeclineMatchRequestIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_match_request_is_declined(self):
        self.client.login(
            username='user1', password='user1')

        self.client.post(
            reverse('decline-match-request', kwargs={'pk': 1}))

        self.assertFalse(MatchRequest.objects.filter(pk=1).exists())


class DeclineMatchInvitationIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_match_invitation_is_declined(self):
        self.client.login(
            username='user1', password='user1')

        self.client.post(
            reverse('decline-match-invitation', kwargs={'pk': 1}))

        invitation = Invitation.objects.get_invitation_by_id(1).first()

        self.assertEqual(invitation.status, 'refused')


class AcceptMatchInvitationIntegrationTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_match_invitation_is_accepted(self):
        self.client.login(
            username='user3', password='user3')
        data = {
            "match_id": 1
        }
        self.client.post(
            reverse('accept-match-invitation', kwargs={'pk': 2}), data)

        invitation = Invitation.objects.get_invitation_by_id(2).first()
        match = Match.objects.get_match_by_id(1).first()
        user = User.objects.get(id=3)

        self.assertEqual(invitation.status, 'accepted')
        self.assertTrue(user.player in match.players.all())
