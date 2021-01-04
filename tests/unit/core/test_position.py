from django.test import TestCase
from core.models.position import Position


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
