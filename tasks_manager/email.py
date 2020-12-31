from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from django.conf import settings


def send_alert_email_for_match(match, recipient_list):

    email_subject = "Invitation pour un match"
    email_body = render_to_string('tasks_manager/alert_email.txt')

    email = EmailMessage(
        email_subject,
        email_body,
        settings.EMAIL_HOST_USER,
        recipient_list
    )
    email.send()
