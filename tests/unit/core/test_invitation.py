from django.test import TestCase
from datetime import datetime
from django.utils.timezone import make_aware

from core.models.invitation import Invitation


class InvitationTest(TestCase):

    fixtures = ["data.json"]

    def test_invitation_instance(self):

        invitation = Invitation.objects.get(id=1)
        self.assertEqual(invitation.status, 'pending')

    def test_invitation_relationship(self):

        invitation = Invitation.objects.get(id=1)

        self.assertEqual(invitation.invitation_date,
                         make_aware(datetime(2020, 1, 1, 1, 0, 0)))
        self.assertEqual(invitation.by_player.firstname, 'user1_firstname')
        self.assertEqual(invitation.for_player.firstname, 'user2_firstname')
        self.assertEqual(invitation.for_match.id, 1)
