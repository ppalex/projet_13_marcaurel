from django.core import mail
from django.test import TestCase

from tasks_manager.email import send_alert_email_for_match


class EmailTest(TestCase):

    fixtures = ["data.json"]

    def test_send_alert_email_for_match(self):
        host_values = {}
        host_values['scheme'] = request.scheme
        host_values['host'] = request.META['HTTP_HOST']

        send_alert_email_for_match(None, ['to@example.com'])

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Invitation pour un match')
