from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from django.conf import settings


def send_alert_email_for_match(match, recipient_list):
    context = {'username': "alex",
               'match_id': match}
    email_subject = "Invitation"
    email_body = render_to_string(
        'tasks_manager/alert_email.txt', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.EMAIL_HOST_USER,
        recipient_list
    )
    email.send()
