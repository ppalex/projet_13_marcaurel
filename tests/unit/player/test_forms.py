from django.test import TestCase
from player.forms.invitation_form import InvitationFormset


class InvitationFormsetTest(TestCase):
    def test_form(self):

        data = {
            'form-INITIAL_FORMS': '0',
            'form-TOTAL_FORMS': '1',
            'form-MAX_NUM_FORMS': '',

            'form-0-username': 'user1'
        }

        form = InvitationFormset(data)

        self.assertTrue(form.is_valid())
