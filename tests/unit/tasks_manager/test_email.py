from django.core import mail
from django.test import TestCase
from unittest import mock

from tasks_manager.email import send_alert_email_for_match


class EmailTest(TestCase):

    fixtures = ["data.json"]

    def test_send_alert_email_for_match(self):

        send_alert_email_for_match(None, ['to@example.com'])

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Invitation pour un match')
