from django.core import mail
from django.test import TestCase
from core.models.match import Match
from tasks_manager.email import send_alert_email_for_match


class EmailTest(TestCase):

    fixtures = ["data.json"]

    def test_send_alert_email_for_match(self):
        host_values = {}
        host_values['scheme'] = "http://"
        host_values['host'] = "localhost:8000/"
        match = Match.objects.get(id=1)
        send_alert_email_for_match(match, ['to@example.com'], host_values)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Invitation')
