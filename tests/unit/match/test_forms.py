from django.test import TestCase
from match.forms.address_creation_form import CustomCreateAddressForm
from match.forms.match_creation_form import CreateMatchForm
from match.forms.match_update_form import UpdateMatchForm

from core.models.match import Match
from django.utils import timezone
from django.core.exceptions import ValidationError


class CustomCreateAddressFormTest(TestCase):
    def test_form(self):

        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles'
        }

        form = CustomCreateAddressForm(data)

        self.assertTrue(form.is_valid())

    def clean_city(self):
        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles'
        }

        form = CustomCreateAddressForm(data)
        if form.is_valid():
            city = form.cleaned_data.get("city")

        self.assertEqual(city, 'bruxelles')

    def clean_street(self):
        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles'
        }

        form = CustomCreateAddressForm(data)
        if form.is_valid():
            street = form.cleaned_data.get("street")

        self.assertEqual(street, 'bruxelles')

    def clean_number(self):
        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles'
        }

        form = CustomCreateAddressForm(data)
        if form.is_valid():
            number = form.cleaned_data.get("number")

        self.assertEqual(number, 1)

    def clean_region(self):
        data = {
            'city': 'bruxelles',
            'street': 'rue des bouchers',
            'number': 1,
            'region': 'bruxelles'
        }

        form = CustomCreateAddressForm(data)
        if form.is_valid():
            region = form.cleaned_data.get("city")

        self.assertEqual(region, 'bruxelles')


class CreateMatchFormTest(TestCase):
    def test_form(self):

        data = {
            'classification': 'private',
            'start_fixture': timezone.now()+timezone.timedelta(hours=1),
            'end_fixture': timezone.now()+timezone.timedelta(hours=2),
            'capacity': 10
        }

        form = CreateMatchForm(data)
        self.assertTrue(form.is_valid())


class UpdateMatchFormTest(TestCase):
    fixtures = ["data.json"]

    def test_form_is_valid(self):

        match = Match.objects.get_match_by_id(1).first()

        data = {
            'classification': 'private',
            'start_fixture': timezone.now()+timezone.timedelta(hours=1),
            'end_fixture': timezone.now()+timezone.timedelta(hours=2),
            'capacity': 10
        }

        form = UpdateMatchForm(data, instance=match)
        self.assertTrue(form.is_valid())

    def test_form_clean_capacity(self):

        match = Match.objects.get_match_by_id(1).first()

        data = {
            'classification': 'private',
            'start_fixture': timezone.now()+timezone.timedelta(hours=1),
            'end_fixture': timezone.now()+timezone.timedelta(hours=2),
            'capacity': 0
        }

        form = UpdateMatchForm(data, instance=match)

        self.assertFalse(form.is_valid())
        self.assertIn('capacity', form.errors.keys())

    def test_form_save(self):

        match = Match.objects.get_match_by_id(1).first()

        data = {
            'classification': 'private',
            'start_fixture': timezone.now()+timezone.timedelta(hours=1),
            'end_fixture': timezone.now()+timezone.timedelta(hours=2),
            'capacity': 8
        }

        form = UpdateMatchForm(data, instance=match)

        if form.is_valid():
            form.save()
            match_saved = Match.objects.get_match_by_id(1).first()

            self.assertEquals(match_saved.available_place, 6)
