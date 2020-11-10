from django.test import TestCase

from datetime import date, datetime
from django.utils.timezone import make_aware
from django.contrib.gis.geos import Point

from core.models.address import Address
from core.models.location import Location
from core.models.position import Position
from core.models.player import Player
from core.models.match import Match


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

    def setUp(self):
        Position.objects.create(
            position_name='keeper'
        )

        Position.objects.create(
            position_name='defensive'
        )

        Position.objects.create(
            position_name='forward'
        )

        Position.objects.create(
            position_name='center'
        )

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

    def setUp(self):

        address = Address.objects.create(
            city="Bruxelles",
            street="rue des bouchers",
            number=1,
            region="Bruxelles"
        )

        location = Location.objects.create(
            coordinates=Point(50, 50, srid=4326)
        )

        position = Position.objects.create(
            position_name='keeper'
        )

        player = Player.objects.create(
            firstname="user1_firstname",
            name='user1_name',
            birthdate=date(2020, 1, 1),
            sex='masculine',
            level='novice',
            address=address,
            location=location
        )

        player.position.add(position)

    def test_player_instance(self):
        player = Player.objects.get(firstname='user1_firstname')

        self.assertEqual(player.firstname, "user1_firstname")
        self.assertIsInstance(player.address, Address)
        self.assertIsInstance(player.location, Location)
        self.assertIsInstance(player.position.first(), Position)
        self.assertEqual(player.location.coordinates.x, 50)
        self.assertEqual(player.location.coordinates.y, 50)


class MatchTestCase(TestCase):
    def setUp(self):

        address = Address.objects.create(
            city="Bruxelles",
            street="rue des bouchers",
            number=1,
            region="Bruxelles"
        )

        location = Location.objects.create(
            coordinates=Point(50, 50, srid=4326)
        )

        player_1 = Player.objects.create(
            firstname="user1_firstname",
            name='user1_name',
            birthdate=date(2020, 1, 1),
            sex='masculine',
            level='novice',
            address=address,
            location=location
        )

        player_2 = Player.objects.create(
            firstname="user2_firstname",
            name='user2_name',
            birthdate=date(2020, 1, 1),
            sex='masculine',
            level='novice',
            address=address,
            location=location
        )

        match = Match.objects.create(
            classification='private',
            fixture=make_aware(datetime(2020, 1, 1, 1, 0, 0)),
            num_player=2,
            capacity=10,
            full=False,
            started=False,
            cancelled=False,
            over=False,
            location=location,
            address=address,
            administrator=player_1
        )

        match.player.add(player_2)

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
        player = players[0]
        self.assertEqual(player.firstname, 'user2_firstname')
