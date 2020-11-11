from django.test import TestCase

from datetime import datetime
from django.utils.timezone import make_aware
from django.contrib.gis.geos import Point

from core.models.address import Address
from core.models.location import Location
from core.models.position import Position
from core.models.player import Player
from core.models.match import Match
from core.models.invitation import Invitation
from core.models.registration import Registration
from core.models.match_request import MatchRequest


class AddressTestCase(TestCase):
    fixtures = ["data.json"]

    def test_address_instance(self):

        address = Address.objects.get(id=1)

        self.assertEqual(address.city, "Bruxelles")
        self.assertEqual(address.street, "rue des bouchers")
        self.assertEqual(address.number, 1)
        self.assertEqual(address.region, "Bruxelles")


class LocationTestCase(TestCase):

    def setUp(self):

        longitude = 50
        latitude = 50

        Location.objects.create(
            coordinates=Point(longitude, latitude, srid=4326)
        )

    def test_location_instance(self):
        location = Location.objects.get(id=1)

        self.assertEqual(location.coordinates.x, 50)
        self.assertEqual(location.coordinates.y, 50)


class PositionTestCase(TestCase):

    fixtures = ["data.json"]

    def test_position_instance(self):

        keeper = Position.objects.get(position_name='keeper')
        defensive = Position.objects.get(position_name='defensive')
        forward = Position.objects.get(position_name='forward')
        center = Position.objects.get(position_name='center')

        self.assertEqual(keeper.position_name, 'keeper')
        self.assertEqual(defensive.position_name, 'defensive')
        self.assertEqual(forward.position_name, 'forward')
        self.assertEqual(center.position_name, 'center')


class PlayerTestCase(TestCase):

    fixtures = ["data.json"]

    def test_player_instance(self):
        player = Player.objects.get(firstname='user1_firstname')

        self.assertEqual(player.firstname, "user1_firstname")
        self.assertIsInstance(player.address, Address)
        self.assertIsInstance(player.position.first(), Position)


class MatchTestCase(TestCase):

    fixtures = ["data.json"]

    def test_match_instance(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        self.assertEqual(match.classification, 'private')

    def test_match_administrator_relationship(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        self.assertEqual(match.administrator.firstname, 'user1_firstname')

    def test_match_player_relationship(self):

        match_queryset = Match.objects.all()
        match = match_queryset[0]

        players = match.player.all()
        player = players[1]

        self.assertEqual(player.firstname, 'user2_firstname')


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


class RegistrationTest(TestCase):
    fixtures = ["data.json"]

    def test_registration_instance(self):

        registration = Registration.objects.get(id=1)
        self.assertEqual(registration.join_date, make_aware(
            datetime(2020, 1, 1, 1, 0, 0)))

    def test_registration_relationship(self):
        registration = Registration.objects.get(id=1)

        self.assertEqual(registration.player.firstname, 'user2_firstname')
        self.assertEqual(registration.match.id, 1)


class MatchResquestTest(TestCase):

    fixtures = ["data.json"]

    def test_match_request_instance(self):
        match_request = MatchRequest.objects.get(id=1)
        self.assertEqual(match_request.request_date, make_aware(
            datetime(2020, 1, 1, 1, 0, 0)))
